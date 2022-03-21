from http.server import BaseHTTPRequestHandler, HTTPServer

with open('app.exe', 'rb') as file:
    app = file.read()

with open('image.jpg', 'rb') as file:
    image = file.read()


class ContentType(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path.endswith('/image'):
            self.send_response(200)
            self.send_header('content-type', 'application/octet-stream')
            self.end_headers()
            self.wfile.write(image)
        if self.path.endswith('/app'):
            self.send_response(200)
            self.send_header('content-type', 'image/jpeg')
            self.end_headers()
            self.wfile.write(image)


if __name__ == '__main__':
    http_server = HTTPServer(('localhost', 8080), ContentType)
    http_server.serve_forever()
