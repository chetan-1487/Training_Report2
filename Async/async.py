import asyncio

# async def main():
#     print('Hello ...',end='')
#     await asyncio.sleep(1)
#     print('... World!')

# asyncio.run(main())



async def nested():
    return 42

async def main():
    task = asyncio.create_task(nested())
    await task

asyncio.run(main())


async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # Simulating an async operation
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    loop = asyncio.get_running_loop()  # Get the current event loop
    print("Starting tasks...")
    
    task1_coro = asyncio.create_task(task1())
    task2_coro = asyncio.create_task(task2())

    await task1_coro
    await task2_coro

    print("All tasks finished.")

asyncio.run(main())
