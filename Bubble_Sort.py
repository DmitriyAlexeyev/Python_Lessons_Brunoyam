list_to_sort = [3, 1, 5, 2, 17, 8, 11, 20, 7, 10]


def bubble_sort(list_to_sort):
    for i in range(len(list_to_sort) - 1):
        for j in range(len(list_to_sort) - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
        print(list_to_sort)


bubble_sort(list_to_sort=list_to_sort)
