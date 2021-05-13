from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(b'1337')

    def do_POST(self):
        var1 = request.form.get('FLAG')
        self._set_headers()
        self.wfile.write(b'ok\n')
        if var1 != '' or 'flag{' in var1:
            print(f"WOW : {var1}")
            

try:
    httpd = HTTPServer(('0.0.0.0', 80), SimpleHTTPRequestHandler)
    httpd.serve_forever()
except KeyboardInterrupt:
    print('Force close')
