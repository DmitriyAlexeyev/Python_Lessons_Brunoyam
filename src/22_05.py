list_to_sort = [3, 1, 87, 5, 2, 17, 43, 8, 23, 11, 20, 7, 10]

# for i in range(len(list_to_sort) - 1):
#     for j in range(len(list_to_sort) - i - 1):
#         if list_to_sort[j] > list_to_sort[j + 1]:
#             list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]
# print(list_to_sort)


sorted_list = []
counter = 0
for i in range(len(list_to_sort) - 1):
    minimum = list_to_sort[0]
    counter += 1
    for j in range(len(list_to_sort) - 1):
        if list_to_sort[j] < minimum:
            minimum = list_to_sort[j]
        print("Несортированный список: ", list_to_sort,
              "Сортированный список: ", sorted_list,
              "Количество итераций: ", counter)
    smallest = minimum
    sorted_list.append(minimum)
    list_to_sort.remove(smallest)
print(list_to_sort, sorted_list, counter)
