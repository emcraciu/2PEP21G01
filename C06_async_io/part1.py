#
import aiohttp
import json
import time
import asyncio


from datetime import datetime

time_zones = []

async def time_getter(session, location='Bucharest', nr=0):
    global time_zones
    while True:
        if nr == len(time_zones):
            response = await session.request(method='GET',
                                             url=f'http://worldtimeapi.org/api/timezone/Europe/{location}')
            my_time = await response.text()
            time_zones.append(json.loads(my_time))
            break
        else:
            time.sleep(0.1)
    return json.loads(my_time)


async def get_word_time():
    async with aiohttp.ClientSession() as session:
        start_time = time.time()
        task = await asyncio.gather(*(time_getter(session, nr=i) for i in range(3)))
        end_time = time.time()
        print(f'total time: {end_time - start_time}')
        print(task[0])


#+asyncio.run(get_word_time())

# async def get_time():
#     await asyncio.sleep(2)
#     print(f'finished time: {datetime.now()}')


# print(type(get_time()))


# async def main():
#     start_time = time.time()
#     await
#     end_time = time.time()
#     print(f'Execution time: {end_time - start_time}')
#
#
# if __name__ == "__main__":
#     asyncio.run(main())
#     # #asyncio.run(main())
#     # result = asyncio.gather(main(), main())
#     # print(type(result))
#     # await result


