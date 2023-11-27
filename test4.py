import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)

player1 = [data[2]]
player1HP = []
print(player1[0]['name'])
if player1[0]['name'] in data[2]['name']:
    print("good")
for i in range(len(data)):
    if player1[0]['name'] in data[i]:
        player1HP.append(data[i]['hp'])
