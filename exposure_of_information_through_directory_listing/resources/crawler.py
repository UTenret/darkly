import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os

SEP = "=" * 40

file_count = 0
lock = asyncio.Lock()


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text(), response.url


async def crawl(url, session):
    html_text, current_url = await fetch(session, url)
    soup = BeautifulSoup(html_text, "html.parser")

    tasks = []

    for link in soup.find_all("a"):
        href = link.get("href")
        if href == "../":
            continue

        full_url = os.path.join(str(current_url), href)

        if href.endswith("/"):
            tasks.append(crawl(full_url, session))
        else:
            tasks.append(check_file(full_url, session))

    await asyncio.gather(*tasks)


async def check_file(url, session):
    html_text, _ = await fetch(session, url)
    if "flag" in html_text:
        async with lock:
            print(f"\n{SEP}\nFound in {url}:\n{html_text.rstrip()}\n{SEP}")

    async with lock:
        global file_count
        file_count += 1
        print(f"\rFiles read: {file_count}", end="")


async def main():
    async with aiohttp.ClientSession() as session:
        await crawl("http://localhost:8080/.hidden/", session)
    print()


if __name__ == "__main__":
    asyncio.run(main())
