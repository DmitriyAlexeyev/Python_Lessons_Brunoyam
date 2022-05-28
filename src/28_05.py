import requests
import time
from threading import Thread
from multiprocessing import Process
import os

# r = requests.get("https://www.youtube.com/")
# print(r.text)

#
# def start_rocket(id):
#     time.sleep(3)
#     print(f"Ракета с id {id} запущена!!!\n")


def func(start, end, timeout):
    while start < end:
        print(f"process {os.getpid()}: {start}")
        start += 1
        time.sleep(timeout)


# threads_list = []
#
# for i in range(5):
#     thread_obj = Thread(target=start_rocket, args=(i, ))
#     threads_list.append(thread_obj)
#
# for i in threads_list:
#     i.start()
#
#
# for i in threads_list:
#     i.join()

if __name__ == '__main__':
    process1 = Process(target=func, args=(3, 10, 1))
    process2 = Process(target=func, args=(5, 20, 0.5))
    process1.start()
    process2.start()

    print('END')

