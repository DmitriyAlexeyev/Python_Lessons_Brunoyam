import json
from Pizzeria import menu

f = open("test.json", "w")
a = json.dump(menu, f)
f.close()
b = json.loads(a)






