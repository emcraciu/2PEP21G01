import requests
import json


def time_getter():
    response = requests.get("http://worldtimeapi.org/api/timezone")
    print('From function: ', type(response))
    my_time_str = response.text
    print('From function: ', type(response))
    return json.loads(my_time_str)


if __name__ == "__main__":
    print(time_getter())
