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

print("\nPlayer 1's cards:\n")
for i in range(5):
    print(player1[i],'\n')

print("\nPlayer 2's cards:\n")
for i in range(5):
    print(player2[i],'\n')

cardUseID = 0
cardAttackID = 0
newCardListID = 0
interactCardListID = 0
specialAtttackDmg = 0
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
        global interactCardListID
        for i in range(len(player2)):
            if cardInteract in player2[i]['name']:
                interactCardListID = i

        if special == 'Y':
            specialAttackDmg = data[cardUseID]['special ability damage']
            interactCardHP = player2[interactCardListID]['hp'] - specialAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP
            if player2[interactCardListID]['hp'] < 1:
                del (player2[interactCardListID])
                print(player2[interactCardListID]['name'],'has died')
                print("player 2's cards are now:\n")
                for i in range(len(player2)):
                    print(player2[i],'\n')
            else:
                print(player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp')
        else:
            normalAttackDmg = data[cardUseID]['damage']
            interactCardHP = player2[interactCardListID]['hp'] - normalAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP
            if player2[interactCardListID]['hp'] < 1:
                del (player2[interactCardListID])
                print(player2[interactCardListID]['name'],'has died')
                print("player 2's cards are now:\n")
                for i in range(len(player2)):
                    print(player2[i],'\n')
            else:
                print(player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp')

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
        global interactCardListID
        for i in range(len(player1)):
            if cardInteract in player1[i]['name']:
                interactCardListID = i

        if special == 'Y':
            specialAttackDmg = data[cardUseID]['special ability damage']
            interactCardHP = player1[interactCardListID]['hp'] - specialAttackDmg
            player1[interactCardListID]['hp'] = interactCardHP
            if player1[interactCardListID]['hp'] < 1:
                del (player1[interactCardListID])
                print(player1[interactCardListID]['name'],'has died')
                print("player 1's cards are now:\n")
                for i in range(len(player1)):
                    print(player1[i],'\n')
            else:
                print(player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp')
        else:
            normalAttackDmg = data[cardUseID]['damage']
            interactCardHP = player1[interactCardListID]['hp'] - normalAttackDmg
            player1[interactCardListID]['hp'] = interactCardHP
            if player1[interactCardListID]['hp'] < 1:
                del (player1[interactCardListID])
                print(player1[interactCardListID]['name'],'has died')
                print("player 1's cards are now:\n")
                for i in range(len(player1)):
                    print(player1[i],'\n')
            else:
                print(player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp')

playerturn = playerTurns()   


while playerCards == 'Alive':
    if firstPlayer == 1:
        playerturn.player1turn()
        playerturn.player2turn()
    else:
        playerturn.player2turn()
        playerturn.player1turn()