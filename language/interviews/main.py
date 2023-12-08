# import threading
# import requests
#
#
# def download_image(url):
#     # Download image by hitting the URL
#     print("Downloading image from {}".format(url))
#     req = requests.get(url)
#
#     # Simulate download
#     import time
#     time.sleep(2)
#     print("Download complete for {}".format(url))
#
#
# def main():
#     # Create threads for downloading images
#     threads = []
#     urls = ["http://example.com/image1.jpg", "http://example.com/image2.jpg", "http://example.com/image3.jpg"]
#     for url in urls:
#         thread = threading.Thread(target=download_image, args=(url,))
#         threads.append(thread)
#         thread.start()
#
#     # Wait for all threads to finish
#     for thread in threads:
#         thread.join()
# if __name__ == "__main__":
#     main()


# How will you implement two threads?
# import threading
# import time
#
#
# def print_even():
#     for i in range(0, 10, 2):
#         print(i)
#         time.sleep(1)


# def print_odd():
#     for i in range(1, 10, 2):
#         print(i)
#         time.sleep(1)
#
#
# def main():
#     t1 = threading.Thread(target=print_even)
#     t2 = threading.Thread(target=print_odd)
#
#     t1.start()
#     t2.start()
#
#     t1.join()
#     t2.join()
#
#
# if __name__ == "__main__":
#     main()

###############################################################

# from multiprocessing import Pool
#
#
# def square(x):
#     return x * x
#
#
# def main():
#     # Create a pool of worker processes
#     pool = Pool(processes=4)
#
#     # Submit tasks to the pool
#     results = pool.map(square, range(10))
#     print(results)
#
#
# if __name__ == "__main__":
#     main()

# how will you implement two multiprocess?
# from multiprocessing import Process
# import time
#
#
# def print_even():
#     for i in range(0, 10, 2):
#         print(i)
#         time.sleep(1)
#
#
# def print_odd():
#     for i in range(1, 10, 2):
#         print(i)
#         time.sleep(1)
#
#
# def main():
#     p1 = Process(target=print_even)
#     p2 = Process(target=print_odd)
#
#     p1.start()
#     p2.start()
#
#     p1.join()
#     p2.join()
#
#
# if __name__ == "__main__":
#     main()

# Can you create multiprocess with pool?
# import time
#
# from multiprocessing import Pool
#
#
# def square(x):
#     return x * x
#
#
# def main():
#     # Create a pool of worker processes
#     pool = Pool(processes=4)
#
#     # Submit tasks to the pool
#     results = pool.map(square, range(10))
#     print(results)
#
#     # Close the pool
#     pool.close()
#     pool.join()
#
#
# if __name__ == "__main__":
#     main()


# Implementing Asynchronous I/O with Two Threads in Python
# import aiohttp
# import asyncio
# import threading
#
#
# async def do_io(url) -> str:
#     """
#     Perform I/O operation asynchronously such as fetching the URL.
#     """
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             response.raise_for_status()
#             return await response.text()
#
#
# def worker(loop, urls):
#     """
#     Worker thread performing I/O operation.
#     """
#     asyncio.set_event_loop(loop)
#     tasks = [do_io(url) for url in urls]
#     result = loop.run_until_complete(asyncio.gather(*tasks))
#     loop.close()
#     print(result)
#
#
# urls = ["https://example.com", "https://example.org"]
#
# # Create two threads
# thread1 = threading.Thread(target=worker, args=(asyncio.new_event_loop(), urls[:1]))
# thread2 = threading.Thread(target=worker, args=(asyncio.new_event_loop(), urls[1:]))
#
# # create multiple threads
# threads_list = []
# for url in urls:
#     thread = threading.Thread(target=worker, args=(asyncio.new_event_loop(), [url]))
#     threads_list.append(thread)
#     thread.start()
#
#
# # Start threads
# thread1.start()
# thread2.start()
#
# # Wait for threads to finish
# thread1.join()
# thread2.join()
