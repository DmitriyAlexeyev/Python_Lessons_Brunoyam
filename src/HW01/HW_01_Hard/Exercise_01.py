# Написать функцию month_to_season(),
# которая принимает 1 аргумент - номер месяца
# - и возвращает название сезона, к которому относится этот месяц.
# Например, передаем 2, на выходе получаем 'Зима'.

def month_to_season(month):
    months = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
    for key, value in months.items():
        if month in value:
            return key


print(month_to_season(6))
print(month_to_season(10))
