import json
import random
from PlayerFunctions import playerTurns
test = open("data.json", encoding="utf8")
data = json.load(test)


player1 = []
player2 = []
length = len(data)

#player deck funtion
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

#define variables
cardUseID = 0
newCardListID = 0
useCardListID = 0
interactCardListID = 0
specialAtttackDmg = 0
firstPlayer = random.randint(1,2)
global playerCards
playerCards = 'Alive'
player1Mana = 0
player2Mana = 0
manaCheck = "no"
playerSet = 'no'
tryAgain = 'test'
global special
special = 'test'
deathListNames = []
specialSet = 'no'
counter = 0
typo1 = 'Yes'
typo2 = 'Yes'
typo3 = 'Yes'
playerturn = playerTurns()


while playerCards == 'Alive':
    if firstPlayer == 1:
        activePlayer = player1
        otherPlayer = player2
        playerturn.player1turn()
        if playerCards =='Dead':
            break
        activePlayer = player2
        otherPlayer = player1
        playerturn.player2turn()
    else:
        activePlayer = player2
        otherPlayer = player1
        playerturn.player2turn()
        if playerCards =='Dead':
            break
        activePlayer = player1
        otherPlayer = player2
        playerturn.player1turn()
    