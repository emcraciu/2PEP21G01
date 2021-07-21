import aiohttp
import json
import time
import asyncio

ZONES = []


async def time_getter(session):
    global ZONES
    while not ZONES:
        await asyncio.sleep(0.1)
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone/Europe/{ZONES.pop(0)}')
    my_time_str = await response.text()
    return json.loads(my_time_str)


async def timezone_getter(session, location='Europe'):
    response = await session.request(method='GET', url=f'http://worldtimeapi.org/api/timezone')
    my_timezone_str = await response.text()
    my_timezone = json.loads(my_timezone_str)
    global ZONES
    ZONES.extend(
        filter(lambda t: t, map(lambda z: z.rsplit('/', maxsplit=1)[-1] if location in z else None, my_timezone)))


async def get_word_time():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        task = await asyncio.gather(timezone_getter(session), *(time_getter(session) for _ in range(10)))
        end_time = time.time()
        print(f'total time: {end_time - start_time}')
        print('Time zone getter writes to global variable and returns:', task[0])
        print('Times are:', *task[1:], sep='\n')


if __name__ == '__main__':
    asyncio.run(get_word_time())
