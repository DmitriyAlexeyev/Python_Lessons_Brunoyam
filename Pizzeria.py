# Администратор (добавляет, удаляет пиццы в меню)
# Пользователь делает заказ (выбирает пиццы, делает заказ)

menu = {
    "Margarita": 400,
    "Pepperoni": 600
}


def add_pizza(name, price):
    if name in menu.keys():
        print("Пицца с таким именем уже есть в меню. Придумайте другое название")
    else:
        menu[name] = price


def remove_pizza(name):
    if name in menu.keys():
        print("Пицца с таким именем есть в меню. Пицца удаляется.")
        del menu[name]
    else:
        print("Пиццы с таким именем нет в меню.")

