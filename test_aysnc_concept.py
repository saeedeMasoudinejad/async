import asyncio

import requests


# This practice demonstrates that the `requests` library is an event loop blocker because when printing all numbers
# between 0 and 19, we expected the execution to finish, but it waits until the `request_method` is fully executed.

async def request_method():
    web_urls = [
        "https://www.bbc.com",
        "https://www.cnn.com",
        "https://www.nytimes.com",
        "https://www.reuters.com",
        "https://www.theguardian.com",
        "https://www.techcrunch.com",
        "https://www.theverge.com",
        "https://www.wired.com",
        "https://www.cnet.com",
        "https://www.arstechnica.com",
        "https://www.khanacademy.org",
        "https://www.coursera.org",
        "https://www.edx.org",
        "https://www.ted.com",
        "https://www.medium.com",
        "https://www.nationalgeographic.com",
        "https://www.sciencenews.org",
        "https://www.smithsonianmag.com",
        "https://www.nature.com",
        "https://www.popularmechanics.com"
    ]
    for url in web_urls:
        requests.get(url)


async def main():
    task = asyncio.create_task(request_method())
    for i in range(20):
        print(i)


asyncio.run(main())
