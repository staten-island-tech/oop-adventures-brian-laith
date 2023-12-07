import json
import random

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


class functions():
    while playerSet == 'no':
                tryAgain = 'test'
                playerSet = 'no'
                specialSet = 'no'
                manaCheck = "no"
                interact = "Y"
                while specialSet == 'no':
                    tryAgain = 'test'
                    playerSet = 'no'
                    specialSet = 'no'
                    manaCheck = "no"
                    interact = 'Y'
                    typo1 = 'Yes'
                    typo2 = 'Yes'
                    typo3 = 'Yes'
                    cardUse = input("State the name of the card you'd like to use: ").title()
                    global special
                    special = input("State whether you'd like to use your card's special ability (Y/N): ").upper()
                    for i in range(len(player1)):
                        if cardUse in player1[i]['name']:
                            typo1 = 'No'
                        if special == 'Y' or special == 'N':
                            typo2 = 'No'
                    if typo1 == "Yes" or typo2 == 'Yes':
                        print("Uh oh someoneeeeeee made a typoooooooooo \nPlease try again:\n")
                    if typo1 == 'No' and typo2 == 'No':
                        if special == 'Y':
                            for i in range(length):
                                if cardUse in data[i]['name']:
                                    cardUseID = i
                            for i in range(len(player1)):
                                if cardUse in player1[i]['name']:
                                    useCardListID = i
                            if player1[useCardListID]['ability type'] == 'self heal' or player1[useCardListID]['ability type'] == 'mass heal':
                                interact = "N"
                                while manaCheck == "no":
                                    if player1[useCardListID]['special ability cost'] <= player1Mana:
                                        player1Mana -= player1[useCardListID]['special ability cost']
                                        manaCheck = 'yes'
                                        specialSet = 'Y'
                                        playerSet = 'Y'
                                    else:
                                        tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ").upper()
                                    if tryAgain == 'N':
                                        special = 'N'
                                        manaCheck = 'yes'
                                        specialSet = 'Y'
                                        playerSet = 'Y'
                                    else:
                                        manaCheck = 'yes'
                                break
                            if player1[useCardListID]['ability type'] == 'aoe':
                                interact = "N"
                                while manaCheck == "no":
                                    if player1[useCardListID]['special ability cost'] <= player1Mana:
                                        player1Mana -= player1[useCardListID]['special ability cost']
                                        manaCheck = 'yes'
                                        specialSet = 'Y'
                                        playerSet = 'Y'
                                    else:
                                        tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ").upper()
                                        if tryAgain == 'N':
                                            special = 'N'
                                            manaCheck = 'yes'
                                            specialSet = 'Y'
                                            playerSet = 'Y'
                                        elif tryAgain == 'Y':
                                            manaCheck = 'yes'
                                if specialSet == 'Y':
                                    break
                            if player1[useCardListID]['ability type'] == 'attack' or player1[useCardListID]['ability type'] == 'single heal':
                                specialSet = 'Y'
                        else:
                            specialSet = 'Y'   
