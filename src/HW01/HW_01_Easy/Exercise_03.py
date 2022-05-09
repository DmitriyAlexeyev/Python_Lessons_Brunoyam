# Напишите программу, которая запрашивала бы у пользователя:
# его имя (например, "What is your name?")
# возраст ("How old are you?")
# место жительства ("Where are you live?")
# После этого выводила бы три строки:
# "This is имя"
#  "It is возраст"
# "(S)he live in место_жительства"
# Вместо имя, возраст, место_жительства должны быть данные, введенные пользователем.

name = input("What is your name?")
age = input("How old are you?")
location = input("Where do you live?")
print("This is", name, "\n",
      "his age is", age, "\n",
      "he lives in", location)
