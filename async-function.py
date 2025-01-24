# In Python, you can create an asynchronous function using the async def syntax.
# Asynchronous functions are used in conjunction with the asyncio library to perform non-blocking operations, such as I/O-bound tasks or network requests.

# Basic Syntax:

import asyncio

async def function_name(parameters):
    # Asynchronous code here
    await some_async_operation()

# async def: Defines an asynchronous function.
# await: Pauses the function execution until the awaited asynchronous operation completes.

async def greet():
    print("Hello")
    await asyncio.sleep(2) # Simulate a delay
    print("World")

asyncio.run(greet())


# 3. Running Multiple Async Functions Concurrently
# You can use asyncio.gather() to run multiple async functions concurrently.

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())

asyncio.run(main())