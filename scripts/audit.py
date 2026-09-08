#!/usr/bin/env python3
import argparse, json, re, socket, ipaddress, sys, time
from html.parser import HTMLParser
from urllib.parse import urlparse, urljoin, urldefrag
from urllib.request import Request, build_opener, HTTPRedirectHandler
from urllib.error import HTTPError, URLError
from pathlib import Path
from collections import Counter, deque

UA="WebGrowthOptimizer/1.0 (+security-bounded-audit)"
MAX_BYTES=2_000_000

class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.title=""; self._in_title=False
        self.metas=[]; self.links=[]; self.headings=[]; self.images=[]; self.scripts=[]
        self.text=[]; self.html_lang=""; self._skip=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs); tag=tag.lower()
        if tag=="html": self.html_lang=a.get("lang","")
        if tag=="title": self._in_title=True
        if tag=="meta": self.metas.append(a)
        if tag=="link": self.links.append(a)
        if tag in ("h1","h2","h3"): self.headings.append([tag,""])
        if tag=="img": self.images.append(a)
        if tag=="script": self.scripts.append(a); self._skip+=1
        if tag in ("style","noscript"): self._skip+=1
    def handle_endtag(self, tag):
        if tag=="title": self._in_title=False
        if tag in ("script","style","noscript") and self._skip: self._skip-=1
    def handle_data(self, data):
        s=" ".join(data.split())
        if not s: return
        if self._in_title: self.title += (" " if self.title else "")+s
        if self.headings and self.lasttag in ("h1","h2","h3"):
            self.headings[-1][1] += (" " if self.headings[-1][1] else "")+s
        if not self._skip: self.text.append(s)

def safe_host(host):
    if not host: return False
    if host.lower() in {"localhost","localhost.localdomain"}: return False
    try:
        infos=socket.getaddrinfo(host, None)
    except socket.gaierror: return False
    for info in infos:
        ip=ipaddress.ip_address(info[4][0])
        if ip.is_private or ip.is_loopback or ip.is_link_local or ip.is_multicast or ip.is_reserved or ip.is_unspecified:
            return False
    return True

class LimitedRedirect(HTTPRedirectHandler):
    max_redirections=5

def fetch(target, timeout=8):
    p=urlparse(target)
    if p.scheme not in ("http","https") or not safe_host(p.hostname): raise ValueError("Unsafe or unsupported target")
    req=Request(target, headers={"User-Agent":UA,"Accept":"text/html,application/xhtml+xml"})
    op=build_opener(LimitedRedirect())
    with op.open(req, timeout=timeout) as r:
        ctype=r.headers.get("Content-Type","")
        data=r.read(MAX_BYTES+1)
        if len(data)>MAX_BYTES: raise ValueError("Response exceeds size limit")
        return r.geturl(), getattr(r,"status",200), dict(r.headers), data.decode("utf-8","replace"), ctype

def meta_value(p, key, value):
    value=value.lower()
    for m in p.metas:
        if m.get(key,"").lower()==value: return m.get("content","").strip()
    return ""

def canonical(p):
    for l in p.links:
        if "canonical" in l.get("rel","").lower(): return l.get("href","").strip()
    return ""

def classify(url,p):
    path=urlparse(url).path.lower(); text=(" ".join(p.text[:80])+" "+p.title).lower()
    rules=[("docs-developer",["/docs","/api","developer","reference"]),("jobs",["/jobs","/careers","job posting"]),
    ("events",["/events","event date","register now"]),("ecommerce",["/product","/shop","add to cart","sku"]),
    ("publisher",["/blog","/news","/article","published"]),("education",["/course","/program","curriculum"]),
    ("real-estate",["/property","/properties","bedroom","sq ft"]),("marketplace",["/listing","/directory","marketplace"]),
    ("saas",["/pricing","/integrations","software","free trial"]),("local",["directions","opening hours","service area"]),
    ("healthcare",["medical","clinic","doctor","patient"])]
    scores={k:sum(1 for x in xs if x in path or x in text) for k,xs in rules}
    k=max(scores,key=scores.get); return k if scores[k]>0 else "general"

def issue(sev,code,msg,evidence="",fix="",confidence="high"):
    return {"severity":sev,"code":code,"message":msg,"evidence":evidence,"fix":fix,"confidence":confidence}

def analyze(url, status, headers, html):
    p=Parser(); p.feed(html)
    text=" ".join(p.text); words=re.findall(r"\b[\w'-]+\b",text)
    desc=meta_value(p,"name","description"); robots=meta_value(p,"name","robots")
    viewport=meta_value(p,"name","viewport"); ogt=meta_value(p,"property","og:title")
    ogd=meta_value(p,"property","og:description"); twt=meta_value(p,"name","twitter:title")
    twd=meta_value(p,"name","twitter:description"); can=canonical(p)
    h1=[x[1].strip() for x in p.headings if x[0]=="h1"]
    imgs_missing=[i.get("src","") for i in p.images if "alt" not in i or not i.get("alt","").strip()]
    jsonld=0; bad_jsonld=0
    for s in re.findall(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>',html,re.I|re.S):
        jsonld+=1
        try: json.loads(s)
        except Exception: bad_jsonld+=1
    issues=[]
    if status>=400: issues.append(issue("Critical","http_status",f"HTTP status {status}",str(status),"Restore a valid crawlable response."))
    if not p.title.strip(): issues.append(issue("High","missing_title","Missing title","","Add a unique descriptive title."))
    if not desc: issues.append(issue("High","missing_meta_description","Missing meta description","","Add a truthful, useful search snippet description."))
    if len(h1)!=1: issues.append(issue("Medium","h1_count",f"Expected one clear H1; found {len(h1)}",str(h1[:3]),"Use one primary page heading."))
    if not can: issues.append(issue("Medium","missing_canonical","No canonical link detected","","Review canonical strategy; add only if appropriate.","medium"))
    if "noindex" in robots.lower(): issues.append(issue("High","noindex","Page contains noindex",robots,"Confirm this is intentional; never auto-remove it.","medium"))
    if not viewport: issues.append(issue("Medium","viewport","Missing viewport meta","","Add a standard responsive viewport meta."))
    if not p.html_lang: issues.append(issue("Low","html_lang","Missing html lang attribute","","Set the document language."))
    if imgs_missing: issues.append(issue("Medium","image_alt",f"{len(imgs_missing)} images missing useful alt text",str(imgs_missing[:5]),"Add contextual alt text to meaningful images; use empty alt for decorative images."))
    if bad_jsonld: issues.append(issue("High","invalid_jsonld",f"{bad_jsonld} JSON-LD block(s) are invalid","","Fix JSON syntax and validate factual claims."))
    if not jsonld: issues.append(issue("Low","no_jsonld","No JSON-LD detected","","Consider appropriate schema only when supported by visible facts.","medium"))
    if not ogt or not ogd: issues.append(issue("Low","open_graph","Open Graph title/description incomplete","","Add social metadata if social sharing matters."))
    if not twt or not twd: issues.append(issue("Low","twitter_meta","Twitter/X title/description incomplete","","Add social card metadata if relevant."))
    if len(words)<150: issues.append(issue("Medium","thin_content",f"Low visible text depth ({len(words)} words)",str(len(words)),"Ensure the page fully satisfies its purpose; do not pad content artificially.","medium"))
    vague=re.findall(r"\b(best|leading|world[- ]class|revolutionary|cutting[- ]edge|very fast|unmatched)\b",text,re.I)
    numbers=re.findall(r"\b\d+(?:\.\d+)?%?\b",text)
    if len(vague)>=2 and len(numbers)==0: issues.append(issue("Medium","citation_quality","Multiple broad claims with little quantified evidence",", ".join(vague[:5]),"Replace unsupported superlatives with specific, attributable evidence where truthful.","medium"))
    qheads=sum(1 for tag,h in p.headings if "?" in h)
    category=classify(url,p)
    score=max(0,100-sum({"Critical":25,"High":12,"Medium":6,"Low":2}[x["severity"]] for x in issues))
    return {"url":url,"status":status,"category":category,"score":score,
      "signals":{"title":p.title.strip(),"title_length":len(p.title.strip()),"description":desc,"description_length":len(desc),
      "h1":h1,"canonical":can,"robots":robots,"word_count":len(words),"images":len(p.images),
      "images_missing_alt":len(imgs_missing),"jsonld_blocks":jsonld,"question_headings":qheads,
      "og_complete":bool(ogt and ogd),"twitter_complete":bool(twt and twd),"html_lang":p.html_lang},
      "issues":issues}

def audit_one(target,timeout):
    if Path(target).exists():
        html=Path(target).read_text(errors="replace"); url=Path(target).resolve().as_uri()
        return analyze(url,200,{},html)
    final,status,headers,html,ctype=fetch(target,timeout)
    return analyze(final,status,headers,html)

def internal_links(base,html):
    p=Parser(); p.feed(html); host=urlparse(base).hostname; out=[]
    for l in p.links:
        pass
    for m in re.finditer(r'<a\b[^>]*href=["\']([^"\']+)["\']',html,re.I):
        u=urldefrag(urljoin(base,m.group(1)))[0]; q=urlparse(u)
        if q.scheme in ("http","https") and q.hostname==host: out.append(u)
    return list(dict.fromkeys(out))

def site_audit(start,max_pages,timeout):
    q=deque([start]); seen=set(); pages=[]
    while q and len(pages)<max_pages:
        u=q.popleft()
        if u in seen: continue
        seen.add(u)
        try:
            final,status,headers,html,ctype=fetch(u,timeout)
            pages.append(analyze(final,status,headers,html))
            for v in internal_links(final,html):
                if v not in seen and len(q)<max_pages*5: q.append(v)
        except Exception as e:
            pages.append({"url":u,"error":str(e),"score":0,"issues":[issue("High","fetch_error",str(e))]})
    titles=Counter(p.get("signals",{}).get("title","") for p in pages if p.get("signals",{}).get("title"))
    duplicates=[t for t,n in titles.items() if n>1]
    return {"mode":"site","start_url":start,"pages_audited":len(pages),"average_score":round(sum(p.get("score",0) for p in pages)/max(1,len(pages)),1),
      "duplicate_titles":duplicates,"pages":pages}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("target"); ap.add_argument("--mode",choices=["quick","full","site"],default="quick")
    ap.add_argument("--max-pages",type=int,default=25); ap.add_argument("--timeout",type=float,default=8)
    ap.add_argument("--output")
    a=ap.parse_args(); t=time.perf_counter()
    try:
        result=site_audit(a.target,max(1,min(a.max_pages,100)),a.timeout) if a.mode=="site" else {"mode":a.mode,"audit":audit_one(a.target,a.timeout)}
        result["runtime_seconds"]=round(time.perf_counter()-t,3); result["engine"]="web-growth-optimizer-zero/1.0"
    except Exception as e:
        result={"error":str(e),"engine":"web-growth-optimizer-zero/1.0"} 
    s=json.dumps(result,indent=2,ensure_ascii=False)
    if a.output: Path(a.output).write_text(s,encoding="utf-8")
    print(s)
if __name__=="__main__": main()
