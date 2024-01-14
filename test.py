import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)

length = len(data) - 1
remove = data[random.randint(0,length)]

print(remove)

data.remove(remove)
print(data)