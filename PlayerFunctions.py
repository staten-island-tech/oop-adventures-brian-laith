import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)


player1 = []
player2 = []
length = len(data)


rand1 = random.sample(range(length-1), 5)
rand2 = random.sample(range(length-1), 5)
for i in range(5):
    player1.extend([data[rand1[i]]])

for i in range(5):
    player2.extend([data[rand2[i]]])

print("\nPlayer one's cards:\n")
for i in range(5):
    print(player1[i],'\n')

print("\nPlayer two's cards:\n")
for i in range(5):
    print(player2[i],'\n')



firstPlayer = random.randint(1,2)
playerCards = 'Alive'
def player1turn():
    for i in range(length):
        print(player1[i], end ='\n')
    cardUse = input("State the name of the card you'd like to use: ")
    special = int(input("State whether you'd like to use your card (Y/N): "))
    cardInteract = (input("State the name of the card you'd like to interact with: "))
    for i in range(len(data)):
        if data[i] == data[cardUse]:
            cardUseID = i
        if data[i] == data[cardInteract]:
            cardInteractID = i
    if special == 'Y':
        specialAttackDmg = data[i]['special ability damage']

    


while playerCards == 'Alive':
    if firstPlayer == 1:
