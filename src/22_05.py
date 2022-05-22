a = [55, 3, 1, 87, 5, 3346, 2, 17, 694, 43, 234, 8, 571, 23, 45, 11, 0, 124, 20, 24, 462, 7, 10]

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

for i in range(len(a) - 1):
    for j in range(len(a) - i - 1):
        if a[j] < a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)


def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

print(factorial(5))
