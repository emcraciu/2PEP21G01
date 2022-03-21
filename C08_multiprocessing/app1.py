import json

import requests

url1 = 'http://worldtimeapi.org/api/timezone/Europe/{}'
url2 = f'http://worldtimeapi.org/api/timezone/'


# #session = requests.Session()
# response = requests.get(url2)
# print(type(response))

def timezone_getter(location='Europe'):
    response = requests.get(url2)
    my_timezone_str = response.text
    my_timezone = json.loads(my_timezone_str)
    return list(
        filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))


if __name__ == '__main__':
    print(timezone_getter())
