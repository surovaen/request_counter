import argparse

import aiohttp
import asyncio
import time


async def get_endpoint(session, url):
    """Асинхронный запрос на эндпоинт."""

    async with session.get(url) as resp:
        return resp


async def main(url):
    """Функция запуска асинхронных запросов на эндпоинт."""

    async with aiohttp.ClientSession() as session:
        tasks = []
        for _ in range(100):
            tasks.append(asyncio.ensure_future(get_endpoint(session, url)))

        await asyncio.gather(*tasks)


if __name__ == '__main__':
    start_time = time.time()

    parser = argparse.ArgumentParser(description='Запуск асинхронных запросов.')
    parser.add_argument('-d', '--domain', type=str, default='127.0.0.1:8000', help='Хост:порт/Домен')
    parser.add_argument('-n', '--number', type=str, default='1', help='Номер метода увеличения счетчика')

    args = parser.parse_args()
    domain = args.domain
    number = args.number
    URL = 'http://{domain}/api/v1/endpoint/counter/{number}/'.format(
        domain=domain,
        number=number,
    )

    asyncio.run(main(URL))
    print("--- %s seconds ---" % (time.time() - start_time))
