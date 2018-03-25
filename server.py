from http.server import BaseHTTPRequestHandler, HTTPServer
import webbrowser

class HTTPServer_Intercom(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text')
        self.end_headers()

    def do_HEAD(self):
        self._set_headers()

    def do_GET(self):
    	pass

    def do_POST(self):
        # Doesn't do anything with posted data
        pass

def run_server():
    print("Starting server http://0.0.0.0:8000/...")

    server_address = ('0.0.0.0', 8000)
    httpd = HTTPServer(server_address, HTTPServer_Intercom)
    print("Running server http://127.0.0.1:8080/...")
    webbrowser.open("http://127.0.0.1:8080/")
    httpd.serve_forever()

run_server()
