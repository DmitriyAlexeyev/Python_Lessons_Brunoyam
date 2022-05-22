list_to_sort = [3, 1, 5, 2, 17, 8, 11, 20, 7, 10]

def find_minimum(list_to_find):
    minimum = list_to_sort[0]
    for i in range(len(list_to_sort) - 1):
        if list_to_sort[i] < minimum:
            minimum = list_to_sort[i]
    return minimum


def selection_sort(list_to_sort):
    sorted_list = []
    for i in range(len(list_to_sort) - 1):
        smallest = find_minimum(list_to_sort[i:])
        sorted_list.append(smallest)
        list_to_sort.remove(smallest)
    print(list_to_sort, sorted_list)


selection_sort(list_to_sort)
