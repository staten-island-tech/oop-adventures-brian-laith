import json
test = open("data.json", encoding="utf8")
data = json.load(test)
print(data)
print(len(data))