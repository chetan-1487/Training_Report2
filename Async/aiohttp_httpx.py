import asyncio
import aiohttp

async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()  # Fetch response body as text

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]  # Create tasks
        responses = await asyncio.gather(*tasks)  # Run tasks concurrently

    for i, response in enumerate(responses):
        print(f"Response {i+1}:\n{response[:100]}...\n")  # Print first 100 chars

asyncio.run(main())  # Run the event loop



import asyncio
import httpx

async def fetch(client, url):
    response=await client.get(url)
    return await response.text  # Fetch response body as text

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3"
    ]

    async with httpx.AsyncClient as client:
        tasks = [fetch(client, url) for url in urls]  # Create tasks
        responses = await asyncio.gather(*tasks)  # Run tasks concurrently

    for i, response in enumerate(responses):
        print(f"Response {i+1}:\n{response[:100]}...\n")  # Print first 100 chars

asyncio.run(main())  # Run the event loop
