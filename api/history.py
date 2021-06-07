from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import json

class handler(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        self._set_response()
        parsed = urlparse(self.path)
        q = parse_qs(parsed.query)
        struct = {
            "symbol": q.get("symbol",["MSFT"])[0],
            "period": q.get("period",["1d"])[0],
            "interval": q.get("interval",["1m"])[0],
        }

        self.wfile.write(json.dumps(struct, indent=2).encode('utf-8'))
        return



if __name__ == '__main__':
    from http.server import HTTPServer
    httpd = HTTPServer(('localhost', 8000), handler)
    httpd.serve_forever()