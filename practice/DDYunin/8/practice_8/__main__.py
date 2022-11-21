import httpx
import time
import threading
import concurrent.futures as cf
from multiprocessing import Process
import asyncio
import aiohttp

def request_httpx_1():
    start_time = time.monotonic()
    for attempt in range(10):
        httpx.get('https://jsonplaceholder.typicode.com/users/{0}'.format(attempt+1))
    print('Время httpx 1 вариант = {0} seconds'.format(time.monotonic() - start_time))

def thread_function(number):
    print('{0} starting'.format(number))
    httpx.get('https://jsonplaceholder.typicode.com/users/{0}'.format(number))
    print('{num} finishing'.format(num=number))


def request_httpx_2():
    start_time = time.monotonic()
    threads = list()
    for index in range(10):
        x = threading.Thread(target=thread_function, args=(index+1,))
        threads.append(x)
        x.start()
    for thread in threads:
        thread.join()
    print('Время httpx 2 вариант (threading) = {0} seconds'.format(time.monotonic() - start_time))

def request_httpx_3():
    start_time = time.monotonic()
    with cf.ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(thread_function, range(1,11))
    print('Время httpx 3 вариант (cf.ThreadPoolExecuter) = {0} seconds'.format(time.monotonic() - start_time))

def process_function(number):
    print('{0} starting proc'.format(number))
    httpx.get('https://jsonplaceholder.typicode.com/users/{0}'.format(number))
    print('{num} finishing proc'.format(num=number))


def request_httpx_4():
    start_time = time.monotonic()
    procs = []
    for num in range(10):
        proc = Process(target=process_function, args=(num+1,))
        procs.append(proc)
        proc.start()
    # complete the processes
    for proc in procs:
        proc.join()
    print('Время httpx 4 вариант (multiprocessing) = {0} seconds'.format(time.monotonic() - start_time))

async def asyncio_function(number):
    print('{0} starting async'.format(number))
    await aiohttp.request('GET', 'https://jsonplaceholder.typicode.com/users/{0}'.format(number))
    print('{num} starting async again'.format(num=number))

def request_httpx_5():
    start_time = time.monotonic()
    ioloop = asyncio.get_event_loop()
    tasks = []
    for number in range(10):
        task = asyncio.ensure_future(asyncio_function(number))
        tasks.append(task)
    wait_tasks = asyncio.wait(tasks)
    ioloop.run_until_complete(wait_tasks)
    ioloop.close()
    print('Время httpx 5 вариант (asincio) = {0} seconds'.format(time.monotonic() - start_time))

def main():
    request_httpx_1()
    request_httpx_2()
    request_httpx_3()
    request_httpx_4()
    request_httpx_5()

if __name__ == '__main__':
    main()