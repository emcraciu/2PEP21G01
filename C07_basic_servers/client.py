import asyncio
import aiohttp


async def phonebook_get(session):
    response = await session.request(method='GET', url='http://localhost:8080/')
    return await response.text()


async def phonebook_add(session: aiohttp.ClientSession, entries: dict):
    response = await session.post(url='http://localhost:8080/add', json=entries)
    return await response.text()


async def phonebook_remove(session: aiohttp.ClientSession, name):
    response = await session.delete(url='http://localhost:8080/remove', json={'entries': [name]})
    return await response.text()


async def phonebook():
    async with aiohttp.ClientSession() as session:
        task = await asyncio.gather(phonebook_get(session),
                                    phonebook_add(session, {'key2': 2}),
                                    phonebook_remove(session, 'key1'))
        print(f'GET: {task[0]}', f'POST: {task[1]}', f'DELETE: {task[2]}', sep='\n')


asyncio.run(phonebook())
