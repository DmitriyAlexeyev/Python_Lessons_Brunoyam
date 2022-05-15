# try:
#     print(100/0)
#
# except:
#     print("Произошла ошибка. На ноль делить нельзя")
#
# a = 1
# b = 2
# print(a + b, "\nЭтот код должен всегда выполняться")


# class MyOwnException(Exception):
#     pass
#
#
# try:
#     raise MyOwnException
# except MyOwnException:
#     print("Обработал")


class ManagerContext:

    def __init__(self, n):
        self.n = n

    def __enter__(self):
        print("__enter__")

        def factorial(n):
            if n == 0:
                return 1
            return n * factorial(n - 1)
        print(factorial(self.n))

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")


with ManagerContext(5) as number:
    print(number)
    print("with")

