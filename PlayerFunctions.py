import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)


player1 = []
player2 = []
length = len(data)

for i in range(5):
    rand1 = random.randint(0,length-1)
    player1.extend([data[rand1]])

for i in range(5):
    rand2 = random.randint(0,length-1)
    player2.extend([data[rand2]])

print('Player one cards:')
for i in range(5):
    print(player1[i], end ='\n')

print('\nPlayer two cards:')
for i in range(5):
    print(player2[i], end ='\n')