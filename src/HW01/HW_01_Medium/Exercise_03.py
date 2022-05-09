# Создать функцию calc(a, b, operation). Описание входных параметров:
# a - Первое число
# b - Второе число
# operation - Действие над ними:
# '+' Сложить
# '-' Вычесть
# '*' Умножить
# '/' Разделить
# В остальных случаях функция должна возвращать "Операция не поддерживается"

def calc(a, b, operation):
    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        return "Операция не поддерживается"


print(calc(3, 2, "+"))
print(calc(3, 2, "-"))
print(calc(3, 2, "*"))
print(calc(3, 2, "/"))
print(calc(3, 2, "?"))
