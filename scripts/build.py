"""Build the static portfolio using an explicit public asset allowlist."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, urlunsplit, parse_qsl, urlencode, unquote
import hashlib, re, shutil
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'dist'
class References(HTMLParser):
    def __init__(self):
        super().__init__(); self.refs=[]
    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in ('src', 'href') and value:
                parsed=urlsplit(value)
                if not parsed.scheme and not parsed.netloc and parsed.path:
                    self.refs.append(unquote(parsed.path))
def build():
    html=(ROOT/'index.html').read_text()
    parser=References(); parser.feed(html)
    files={'index.html', *parser.refs}
    pending=list(files)
    while pending:
        name=pending.pop()
        path=ROOT/name
        if not path.is_file(): raise SystemExit('Missing asset: '+name)
        if path.suffix=='.css':
            for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',path.read_text()):
                child=(path.parent/unquote(ref)).resolve().relative_to(ROOT).as_posix()
                if child not in files: files.add(child); pending.append(child)
    # Only the generated output directory is replaced; original legacy files stay in place.
    if OUT.exists(): shutil.rmtree(OUT)
    OUT.mkdir()
    for name in sorted(files):
        dest=OUT/name; dest.parent.mkdir(parents=True,exist_ok=True)
        shutil.copy2(ROOT/name,dest)
    # Fingerprint stylesheet/script requests so a rebuild never mixes old code
    # with new markup in an already-open browser tab.
    def version_asset(match):
        parsed=urlsplit(match[2])
        if parsed.scheme or parsed.netloc or Path(parsed.path).suffix not in ('.css', '.js'):
            return match[0]
        asset=ROOT/unquote(parsed.path)
        version=hashlib.sha256(asset.read_bytes()).hexdigest()[:12]
        query=[(key,value) for key,value in parse_qsl(parsed.query) if key!='v']
        query.append(('v',version))
        url=urlunsplit((parsed.scheme,parsed.netloc,parsed.path,urlencode(query),parsed.fragment))
        return f'{match[1]}="{url}"'
    html=re.sub(r'(href|src)="([^"]+)"',version_asset,html)
    (OUT/'index.html').write_text(html)
    print(f'Built {len(files)} public files in {OUT}')
if __name__=='__main__': build()
