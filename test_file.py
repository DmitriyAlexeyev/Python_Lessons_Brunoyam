import json

# f = open("test.json", "w")
# a = json.dump(menu, f)
# f.close()
# b = json.loads(a)


f = open("test.json", "r")
a = json.load(f)
print(a)
f.close()



