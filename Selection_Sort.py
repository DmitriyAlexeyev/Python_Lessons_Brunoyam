list_to_sort = [55, 3, 1, 87, 5, 3346, 2, 17, 694, 43, 234, 8, 571, 23, 45, 11, 0, 124, 20, 24, 462, 7, 10]


def find_minimum(list_to_find):
    minimum = list_to_sort[0]
    for i in range(len(list_to_sort)):
        if list_to_sort[i] < minimum:
            minimum = list_to_sort[i]
    return minimum


def selection_sort(list_to_sort):
    sorted_list = []
    for i in range(len(list_to_sort)):
        smallest = find_minimum(list_to_sort[i:])
        sorted_list.append(smallest)
        list_to_sort.remove(smallest)
    print(sorted_list)


selection_sort(list_to_sort)
