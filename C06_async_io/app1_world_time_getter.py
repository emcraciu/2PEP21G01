import aiohttp
import json
import time
import asyncio


async def time_getter(session, location='Bucharest'):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
    my_time_str = await response.text()
    return json.loads(my_time_str)


async def timezone_getter(session, location='Europe'):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone')
    my_timezone_str = await response.text()
    my_timezone = json.loads(my_timezone_str)
    return filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone))


async def get_word_time():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        task = await asyncio.gather(timezone_getter(session), *(time_getter(session) for _ in range(3)))
        end_time = time.time()
        print(f'total time: {end_time - start_time}')
        print('Zones are:', list(task[0]))
        print('Times are:', *task[1:], sep='\n')


if __name__ == '__main__':
    asyncio.run(get_word_time())

Romeo
from http.server import HTTPServer, BaseHTTPRequestHandler

with open('index.html') as file:

html = file.read
()

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


http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
http_server.serve_forever()
19: 07
Delia
Dragos


def do_POST(self):
    if self.path.endswith('/add'):
        print('Anything')


import cgi
from http.server import HTTPServer, BaseHTTPRequestHandler

with open('index.html') as file:
    html =
file.read
()

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
            # content_type,data=cgi.parse_header(self.headers.get('content-type'))
            # print(content_type,data)
            # data['boundary']=bytes(data['boundary'],'utf-8')
            # c_len=int(self.headers.get('Content-length'))
            # data['CONTENT-LENGTH']=c_len
            print(cgi.parse(self.rfile))

            # print(self.headers.get('content-type'))

        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()

    def do_DELETE(self):
        if self.path.endswith('/add'):
            print('Remove')
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()


http_server = HTTPServer(('localhost', 8080), WebPhoneBook)
http_server.serve_forever()
import asyncio
import aiohttp
import time


async def phonebook_getter(session):
    response = await session.request(method='GET', url='
    http: // localhost: 8080 /
                        ')
    my_phonebook = await response.text()
    return my_phonebook


async def phonebook_getter2():
    async with aiohttp.ClientSession() as session:
        task = await asyncio.gather(phonebook_getter(session), phonebook_add(session, {'key2': 2}),
                                    phonebook_remove(session, 'key1'))
        print(task)


async def phonebook_add(session: aiohttp.ClientSession, entries: dict):
    respose = await


session.post
(url='
http: // localhost:8080 / add
', json=entries)
my_phonebook = await respose.text()
time.sleep(2)
return my_phonebook


async def phonebook_remove(session: aiohttp.ClientSession, name):
    response = await session.delete(url='
    http: // localhost: 8080 / remove
    ', json={'
    entries
    ': [name]})
    my_phonebook = await response.text()
    return my_phonebook


asyncio.run
(phonebook_getter2())
20: 54
Bogdan
from http.server import HTTPServer, BaseHTTPRequestHandler

with open('image.jpg', 'rb') as file:
    image =
file.read
()


class ImageLoad(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'image/jpeg')
        self.end_headers()
        self.wfile.write(image)


http_server = HTTPServer(('localhost', 8080), ImageLoad)
http_server.serve_forever()
21: 06
https: // stackoverflow.com / questions / 41459168 / which - mime - type - is -correct -
for -the - exe - file
    21: 13
Bogdan
from http.server import HTTPServer, BaseHTTPRequestHandler

with open('putty.exe', 'rb') as file:
    app =
file.read
()


class ImageLoad(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'application/octet-stream')
        self.end_headers()
        self.wfile.write(app)


http_server = HTTPServer(('localhost', 8080), ImageLoad)
http_server.serve_forever()