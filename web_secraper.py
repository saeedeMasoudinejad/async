import requests
from bs4 import BeautifulSoup
import asyncio


async def get_web_content(web_url: str) -> str:
    # print("fetch is done")
    try:
        response = requests.get(web_url)
    except requests.exceptions.Timeout:
        response = requests.get(web_url)
    except requests.exceptions.ConnectionError:
        response = requests.get(web_url)
    except requests.exceptions.TooManyRedirects:
        return
    html_content = response.text
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup


def fetch_html_element_content(html_content: str, html_element: str) -> str:
    return html_content.find(html_element)


def write_on_file(element_content: str) -> None:
    # Specify the file name (it will create a new file if it doesn't exist)
    file_name = "example_file.txt"
    with open(file_name, 'w') as file:
        file.write(element_content)


# soup = get_web_content(web_urls[0])
# print(soup)
# div_content =fetch_html_element_content(soup, 'div')
# print(div_content)
# a_content = fetch_html_element_content(soup, 'a')
# fetch_html_element_content(soup, div_content)

async def main():
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
    # web_html_content = list()
    # tasks = [get_web_content(url) for url in web_urls]
    # result = asyncio.gather(*tasks)
    for url in web_urls:
        task = asyncio.create_task(get_web_content(url))
        # await task


if __name__ == "__main__":
    from time import perf_counter

    time_duration = list()
    for i in range(3):
        start = perf_counter()
        asyncio.run(main())
        end = perf_counter()
        time_duration.append(end - start)
    print(sum(time_duration) / 3)
    # main()
# sync ------------------------>27.64769868098665
# async ----------------------->30.29525362533362
# asyn_with_gathering --------> 28.16176266669451
