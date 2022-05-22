a = [55, 3, 1, 87, 5, 3346, 2, 17, 694, 43, 234, 8, 571, 23, 45, 11, 0, 124, 20, 24, 462, 7, 10]


def merge_sort(unsorted_list):
    if len(unsorted_list) < 2:
        return unsorted_list
    medium_index = len(unsorted_list) // 2

    left_list = merge_sort(unsorted_list[:medium_index])
    right_list = merge_sort(unsorted_list[medium_index:])
    return merge(left_list, right_list)


def merge(left_list, right_list):
    result = []
    i, j = 0, 0
    while len(left_list) > i and len(right_list) > j:
        if left_list[i] < right_list[j]:
            result.append(left_list[i])
            i += 1
        else:
            result.append(right_list[j])
            j += 1
    while len(left_list) > i:
        result.append(left_list[i])
        i += 1
    while len(right_list) > j:
        result.append(right_list[j])
        j += 1
    return result


print(merge_sort(a))
