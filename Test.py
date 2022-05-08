users = {"admin": "1234"}
secret_info = "42"


def login_password():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    return login, password


def enter():
    login, password = login_password()
    if login in users.keys():
        if users[login] == password:
            print("Успешный вход!", "\n", secret_info)
    print("Данный логин отсутствует.")


def register():
    login, password = login_password()
    if login in users.keys():
        print("Логин занят!")
    else:
        users[login] = password
        print("Регистрация прошла успешно!")


def delete():
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    if login in users.keys():
        if users[login] == password:
            del users[login]
            print("Успешное удаление!")
    #         break
    else:
        print("Данный логин отсутствует.")


def error():
    print("Ошибка ввода!")


while True:
    q1 = input("Вход, Регистрация или Удаление?")
    if q1 == "Вход":
        enter()
        break
    elif q1 == "Регистрация":
        register()
    elif q1 == "Удаление":
        delete()
    else:
        error()


# while True:
#     q1 = input("Вход, Регистрация или Удаление?")
#     if q1 == "Вход":
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#         if login in users.keys():
#             if users[login] == password:
#                 print("Успешный вход!", "\n", secret_info)
#                 break
#         print("Данный логин отсутствует.")
#     elif q1 == "Регистрация":
#         login = input("Введите логин:")
#         password = input("Введите пароль:")
#         if login in users.keys():
#             print("Логин занят!")
#         else:
#             users[login] = password
#             print("Регистрация прошла успешно!")
#     elif q1 == "Удаление":
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#         if login in users.keys():
#             if users[login] == password:
#                 del users[login]
#                 print("Успешное удаление!")
#         #         break
#         else:
#             print("Данный логин отсутствует.")
#     else:
#         print("Ошибка ввода!")
