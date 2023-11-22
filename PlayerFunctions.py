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
player1HP = []
player2HP = []



for i in range(length):
    if player1[0]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[1]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[2]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[3]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[4]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])

for i in range(length):
    if player2[0]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[1]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[2]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[3]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[4]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])




class playerTurns():
    def player1turn(self):
        print("Player 1's turn!\n")
        cardUse = input("State the name of the card you'd like to use: ")
        special = (input("State whether you'd like to use your card's special ability (Y/N): "))
        cardInteract = (input("State the name of the card you'd like to interact with: "))
        for i in range(length):
            if cardUse in data[i]['name']:
                cardUseID = i
            if cardUse in data[i]['name']:
                cardAttackID = i

        for i in range(len(player2)):
            if cardInteract in player2[i]:
                interactCardListID = i

        if special == 'Y':
            specialAttackDmg = data[cardUseID]['special ability damage']
            interactCardHP = interactCardListID - specialAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP
        else:
            normalAttackDmg = player1[cardUseID]['damage']
            interactCardHP = interactCardListID - normalAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP

    def player2turn(self):
        print("Player 2's turn!\n")
        cardUse = input("State the name of the card you'd like to use: ")
        special = (input("State whether you'd like to use your card's special ability (Y/N): "))
        cardInteract = (input("State the name of the card you'd like to interact with: "))
        for i in range(length):
            if cardUse in data[i]['name']:
                cardUseID = i
            if cardUse in data[i]['name']:
                cardAttackID = i

        for i in range(len(player1)):
            if cardInteract in player1[i]:
                interactCardListID = i

        if special == 'Y':
            specialAttackDmg = data[cardUseID]['special ability damage']
            interactCardHP = interactCardListID - specialAttackDmg
            player1[interactCardListID]['hp'] = interactCardHP
        else:
            normalAttackDmg = player2[cardUseID]['damage']
            interactCardHP = interactCardListID - normalAttackDmg
            player1[interactCardListID]['hp'] = interactCardHP

playerturn = playerTurns()   


while playerCards == 'Alive':
    if firstPlayer == 1:
        playerturn.player1turn()
        playerturn.player2turn()
    else:
        playerturn.player2turn()
        playerturn.player1turn()