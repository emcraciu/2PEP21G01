from http.server import HTTPServer, BaseHTTPRequestHandler

with open('index.html') as file:
    html = file.read()

phone_book = {'key1': 1}


class WebPhoneBook(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

        content = ''
        for name, number in phone_book.items():
            content += f"""
    <tr>
        <td align="left">{name}</td>
        <td align="left">{number}</td>
    </tr>
"""
        self.wfile.write(html.format(content).encode())

    def do_POST(self):
        if self.path.endswith('/add'):
            print(self.parse_request())
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()

    def do_DELETE(self):
        if self.path.endswith('/remove'):
            self.send_response(200)
            self.send_header('content-type', 'application/json')
            self.end_headers()


if __name__ == '__main__':
    http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
    http_server.serve_forever()
