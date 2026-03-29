from http.server import BaseHTTPRequestHandler, HTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        message = "Hello from DevOps CI/CD Pipeline 🚀 (Python)"
        self.wfile.write(message.encode("utf-8"))
server = HTTPServer(('0.0.0.0', 3000), Handler)

print("Server running on port 3000...")
server.serve_forever()
