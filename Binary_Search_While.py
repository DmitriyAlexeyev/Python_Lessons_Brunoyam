# def recursive_binary_search(search_list, find):
#     left = 0
#     right = len(search_list) - 1
#     median = len(search_list)//2
#     element = search_list[median]
#     if find < element:
#         right = median
#         search_list = search_list[:right]
#         recursive_binary_search(search_list, find)
#     elif find > element:
#         left = median
#         search_list = search_list[left:]
#         recursive_binary_search(search_list, find)
#     elif find == element:
#         print(search_list[median])
#
#
# recursive_binary_search(search_list=search_list, find=17)


search_list = [1, 2, 3, 5, 7, 10, 11, 12, 17, 18, 20, 22, 25, 27, 30]


def binary_search(search_list, find):
    left = 0
    right = len(search_list) - 1
    counter = 0
    while left <= right:
        counter += 1
        median = (left + right)//2
        if search_list[median] == find:
            print(search_list[median], counter)
            break
        elif find < search_list[median]:
            right = median - 1
        elif find > search_list[median]:
            left = median + 1

binary_search(search_list=search_list, find=1)
binary_search(search_list=search_list, find=3)
binary_search(search_list=search_list, find=7)
binary_search(search_list=search_list, find=11)
binary_search(search_list=search_list, find=17)
binary_search(search_list=search_list, find=20)
binary_search(search_list=search_list, find=25)
binary_search(search_list=search_list, find=27)
binary_search(search_list=search_list, find=30)





