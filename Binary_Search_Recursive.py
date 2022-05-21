
# def factorial(n):
#     return 1 if n == 0 else n * factorial(n - 1)
#
#
# print(factorial(16))


# class ManagerContext:
#
#     def __init__(self, n):
#         self.n = n
#
#     def __enter__(self):
#         print("__Enter__")
#
#         def factorial(n):
#             return 1 if n == 0 else n * factorial(n - 1)
#         print(factorial(self.n))
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("__Exit__")
#
#
# with ManagerContext(64) as number:
#     print(number)

search_list = [1, 2, 3, 5, 7, 10, 11, 12, 17, 18, 20, 22, 25, 27, 30]


def recursive_binary_search(search_list, find, counter):
    left_index = 0
    right_index = len(search_list) - 1
    median_index = (left_index + right_index)//2
    found_element = search_list[median_index]
    counter += 1
    if find < found_element:
        right_index = median_index
        search_list = search_list[:right_index]
        recursive_binary_search(search_list, find, counter)
    elif find > found_element:
        left_index = median_index
        search_list = search_list[left_index:]
        recursive_binary_search(search_list, find)
    elif find == found_element:
        print(search_list[median_index])
        print(counter)


try:
    recursive_binary_search(search_list=search_list, find=1, counter=0)
except RecursionError:
    print("Элемент не найден")



