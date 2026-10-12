"""Build and serve only the public files on loopback. Stop with Ctrl+C."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import argparse
from build import build, OUT
parser=argparse.ArgumentParser();parser.add_argument('--port',type=int,default=8765);args=parser.parse_args()
build()
handler=partial(SimpleHTTPRequestHandler,directory=str(OUT))
print(f'Local portfolio: http://127.0.0.1:{args.port}',flush=True)
with ThreadingHTTPServer(('127.0.0.1',args.port),handler) as server:
    try:server.serve_forever()
    except KeyboardInterrupt:print('\nPreview stopped.')
