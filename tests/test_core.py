import json, subprocess, sys, tempfile
from pathlib import Path
html="""<!doctype html><html lang="en"><head><title>Example SaaS</title><meta name="description" content="Useful software page"><meta name="viewport" content="width=device-width,initial-scale=1"></head><body><h1>Example SaaS</h1><p>"""+"word "*200+"""</p></body></html>"""
with tempfile.TemporaryDirectory() as d:
 p=Path(d)/"x.html"; p.write_text(html)
 r=subprocess.run([sys.executable,str(Path(__file__).parents[1]/"scripts"/"audit.py"),str(p),"--mode","quick"],capture_output=True,text=True,check=True)
 j=json.loads(r.stdout); assert j["audit"]["score"]>0; assert j["engine"].startswith("web-growth")
print("zero_dependency_test: PASS")
