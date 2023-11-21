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


cardUseID = 1
cardAttackID = 1
newCardListID = 1
firstPlayer = random.randint(1,2)
playerCards = 'Alive'
nextListPart = 0
player1HP = []
player2HP = []

for i in range(5):
    for i in range(length):
        if player1[nextListPart]['name'] in data[i]['name']:
            player1HP.append(data[i]['health'])
            nextListPart += 1
print(player1HP)



def player1turn():
    for i in range(length):
        print(player1[i], end ='\n')
    cardUse = input("State the name of the card you'd like to use: ")
    special = int(input("State whether you'd like to use your card (Y/N): "))
    cardInteract = (input("State the name of the card you'd like to interact with: "))
    for i in range(length):
        if cardUse in data[i]['name']:
            cardUseID = i
        if cardUse in data[i]['name']:
            cardAttackID = i

    for i in range(len(player2)):
        if cardInteract in player2[i]:
            newCardListID = i
    
    if special == 'Y':
        specialAttackDmg = data[cardUseID]['special ability damage']

        


while playerCards == 'Alive':
    if firstPlayer == 1:
        print('Hi')