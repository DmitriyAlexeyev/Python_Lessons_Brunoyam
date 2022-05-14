# Администратор (добавляет, удаляет пиццы в меню)
# Пользователь делает заказ (выбирает пиццы, делает заказ)
#
# menu = {
#     "Margarita": 400,
#     "Pepperoni": 600
# }

import json
# with open("test.json", "r") as f:
#     menu = json.load(f)


def load_menu():
    f = open("test.json", "r")
    menu = json.load(f)
    f.close()
    return menu


def save_menu(menu):
    f = open("test.json", "w")
    json.dump(menu, f)
    f.close()


def add_pizza(name, price):
    menu = load_menu()
    if name in menu.keys():
        print("Пицца с таким именем уже есть в меню. Придумайте другое название")
    else:
        menu[name] = price
    save_menu(menu)


def remove_pizza(name):
    menu = load_menu()
    if name in menu.keys():
        print("Пицца с таким именем есть в меню. Пицца удаляется.")
        del menu[name]
    else:
        print("Пиццы с таким именем нет в меню.")

    save_menu(menu)


def order_pizza():
    menu = load_menu()
    order = []
    cost = 0
    while True:
        q1 = input("Продолжить заказ? (yes/no)")
        if q1 == "No":
            break
        else:
            print("Наше меню: ", "\n", menu)
            pizza_name = input("Выберите пиццу.")
            if pizza_name in menu.keys():
                order.append(pizza_name)
                cost += menu[pizza_name]
                print("Пицца добавлена в заказ", "\n", "Сумма заказа: {}".format(cost))
    return {"order": order, "cost": cost}


if __name__ == "__main__":
    while True:
        q3 = input("Продолжить? (yes/no)")
        if q3 == "yes":
            role = input("Выберите роль.")
            if role == "admin":
                q2 = input("Добавить или удалить? (add/remove)")
                if q2 == "add":
                    pizza_name = input("Введите имя пиццы.")
                    pizza_price = int(input("Введите стоимость пиццы."))
                    add_pizza(name=pizza_name, price=pizza_price)
                elif q2 == "remove":
                    pizza_name = input("Введите имя удаляемой пиццы.")
                    remove_pizza(name=pizza_name)
            elif role == "user":
                print(order_pizza())
            else:
                print("Ошибка ввода.")
        elif q3 == "no":
            break
        else:
            print("Ошибка ввода.")
