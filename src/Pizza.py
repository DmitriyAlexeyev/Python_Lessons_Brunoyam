import json


class Pizzeria:

    @staticmethod
    def load_menu():
        f = open("menu.json", "r")
        menu = json.load(f)
        f.close()
        return menu

    @staticmethod
    def __save_menu(menu):
        f = open("menu.json", "w")
        json.dump(menu, f)
        f.close()

    def add_pizza(self, name, price):
        menu = self.load_menu()
        if name in menu.keys():
            print("Пицца с таким именем уже есть в меню. Придумайте другое название")
        else:
            menu[name] = price
        self.__save_menu(menu)

    def remove_pizza(self, name):
        menu = self.load_menu()
        if name in menu.keys():
            print("Пицца с таким именем есть в меню. Пицца удаляется.")
            del menu[name]
        else:
            print("Пиццы с таким именем нет в меню.")
        self.__save_menu(menu)

    def order_pizza_api(self, order):
        menu = self.load_menu()
        cost = 0
        for pizza_name in order:
            if pizza_name in menu.keys():
                cost += menu[pizza_name]
            else:
                return None
        return cost


    def order_pizza(self):
        menu = self.load_menu()
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


pizzeria = Pizzeria()

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
                    pizzeria.add_pizza(name=pizza_name, price=pizza_price)
                elif q2 == "remove":
                    pizza_name = input("Введите имя удаляемой пиццы.")
                    pizzeria.remove_pizza(name=pizza_name)
            elif role == "user":
                print(pizzeria.order_pizza())
            else:
                print("Ошибка ввода.")
        elif q3 == "no":
            break
        else:
            print("Ошибка ввода.")
