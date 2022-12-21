import gevent.monkey
from urllib.request import urlopen
from datetime import datetime
import anyio
from asyncer import asyncify

gevent.monkey.patch_all()
urls = ['http://www.google.com',
        'http://www.yandex.ru',
        'http://www.python.org',
        'http://vc.ru',
        'http://d3.ru',
        'http://mongo.one']


def get_url(url):
    try:
        data = urlopen(url).read()

        if data:
            return data
    except:
        pass
    return ""


start = datetime.now()
for i in range(1, 10):
    jobs = [gevent.spawn(get_url, _url) for _url in urls]
    gevent.wait(jobs)
print(datetime.now() - start)


async def get_urls():
    for url in urls:
        data = await asyncify(get_url)(url=url)


start = datetime.now()
anyio.run(get_urls)
print(datetime.now() - start)
