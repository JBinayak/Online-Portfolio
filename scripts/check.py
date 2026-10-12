"""Check navigable anchors, asset paths, accessibility basics and stale/private content."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import re
ROOT=Path(__file__).resolve().parents[1]
class Page(HTMLParser):
    def __init__(self):
        super().__init__();self.ids=[];self.refs=[];self.images=[];self.h1=0;self.html={}
    def handle_starttag(self,tag,attrs):
        attrs=dict(attrs)
        if tag=='html': self.html=attrs
        if 'id' in attrs:self.ids.append(attrs['id'])
        if tag=='h1':self.h1+=1
        if tag=='img':self.images.append(attrs)
        for attr in ('href','src'):
            if attrs.get(attr):self.refs.append(attrs[attr])
source=(ROOT/'index.html').read_text();page=Page();page.feed(source)
errors=[]
if len(page.ids)!=len(set(page.ids)):errors.append('Duplicate IDs')
if page.h1!=1:errors.append('Expected one primary heading')
if page.html.get('lang')!='en':errors.append('Missing page language')
for im in page.images:
    if 'alt' not in im:errors.append('Image without alt text')
for ref in page.refs:
    u=urlsplit(ref)
    if u.scheme or u.netloc:continue
    if u.path and not (ROOT/unquote(u.path)).is_file():errors.append('Missing local file: '+ref)
    if not u.path and u.fragment and u.fragment not in page.ids:errors.append('Missing anchor: '+ref)
    if ref=='#':errors.append('Placeholder link')
for pattern in [r'Lorem ipsum',r'Proin gravida',r'CV not made',r'need-to-create',r'tel:',r'309.{0,8}631',r'980866',r'980804',r'December 24, 2004']:
    if re.search(pattern,source,re.I):errors.append('Stale or private content found: '+pattern)
for css in ['css/portfolio.css']:
    path=ROOT/css
    for ref in re.findall(r'url\([\'\"]?([^\)\'\"]+)',path.read_text()):
        if not (path.parent/unquote(ref)).is_file():errors.append('Missing CSS asset: '+ref)
if errors:raise SystemExit('\n'.join(errors))
print(f'Checks passed: {len(page.refs)} references, {len(page.ids)} unique IDs, image alternatives, no known private/stale content.')
