# Напишите программу, которая будет выводить нечетные числа из списка и остановится, если встретит число 139
number = 0
while number <= 139:
    if number % 2 != 0:
        print(number)
    number += 1