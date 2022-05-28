import requests
import asyncio
import aiohttp
from datetime import datetime

resource_list = ["https://github.com/",
                 "https://www.youtube.com/",
                 "https://pythonru.com/",
                 "https://spring.io/",
                 "https://vk.com/",
                 "https://javarush.ru/",
                 "https://ru.wikipedia.org/",
                 "https://yandex.ru/"]

sync_t1 = datetime.now()
for resource in resource_list:
    r = requests.get(resource)
    print(len(r.text))
sync_t2 = datetime.now()
sync_delta = sync_t2 - sync_t1
print(f'Sync Time {sync_delta.microseconds}')



async def get_data(url):
    print(f"Start {url}")
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            print(len(data))


t1 = datetime.now()
jobs = [get_data(url) for url in resource_list]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(jobs))
t2 = datetime.now()

delta = t2 - t1
print(f"Time {delta.microseconds}")
print(f"Difference {sync_delta.microseconds/delta.microseconds}")
