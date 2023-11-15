import json
import random
test = open("data.json", encoding="utf8")
data = json.load(test)
player1 = []
player2 = []

for i in range(5):
    card = random.randint(0,len(data)-1)
    player1.append(data[card])
for i in range(5):
    card = random.randint(0,len(data)-1)
    player2.append(data[card])

print('Player 1 Cards: ',player1,'Player 2 Cards: ',player2)
