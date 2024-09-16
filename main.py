import asyncio
import datetime

async def fetch_date():
    print("start fetching ....")
    await asyncio.sleep(3)
    print("end fetching.")

async def print_numbers(number: int):
    for i in range(number):
        asyncio.sleep()

def test_sync():
    print("this is the sync function")


asyncio.run(main(datetime.datetime.now()))
# print(type(await test_async()))
# print(type(test_sync()))