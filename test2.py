import json
import random
test = open("data.json", encoding="utf8")
data = json.load(test)
player1 = []
player2 = []
cardUse = input("test: ")
x= len(data)
for i in range(x):
    if cardUse in data[i]['name']:
        player1.extend([data[i]["name"]])

print(player1)