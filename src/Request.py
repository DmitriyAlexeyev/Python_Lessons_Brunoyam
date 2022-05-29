from bs4 import BeautifulSoup
import requests



# menu = requests.get("http://127.0.0.1:5000/pizzeria/menu", params={"pizza_name": "vesuvium"})
# # print(menu.status_code)
# if menu.status_code != 404:
#     print(menu.json())
# else:
#     print("Пиццы не существует")

# r = requests.post("http://127.0.0.1:5000/pizzeria/menu/pizza", data={"name": "vesuvium", "cost": 600})
# print(r.status_code)

# menu = requests.get("http://127.0.0.1:5000/pizzeria/menu")
# print(menu.json())
#
# r = requests.delete("http://127.0.0.1:5000/pizzeria/menu/pizza", params={"pizza_name": "vesuvium"})
# print(r.status_code)

cost = requests.post("http://127.0.0.1:5000/pizzeria/order", data={"order": ["margarita", "pepperoni"]})
print(cost.json())

