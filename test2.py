import json
import random
test = open("data.json", encoding="utf8")
data = json.load(test)
player1 = []
player2 = []
cardUse = str(input("test: "))
print(data[1][cardUse])
if data[1]["name"] == data[1][cardUse]:
    print("good")