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
tryAgain = 'N'
global special
special = 'test'





class playerTurns():
    def player1turn(self):
        global player1Mana
        player1Mana += 2
        print("Player 1's turn!\n")
        print("\nYour cards:\n")
        for i in range(len(player1)):
            print(player1[i],'\n')
        print("You have",player1Mana,"mana \n")
        playerSet = 'no'
        while playerSet == 'no':
            tryAgain = 'test'
            playerSet = 'no'
            manaCheck = "no"
            cardUse = input("State the name of the card you'd like to use: ")
            global special
            special = input("State whether you'd like to use your card's special ability (Y/N): ")
            cardInteract = input("State the name of the card you'd like to interact with: ")
            for i in range(length):
                if cardUse in data[i]['name']:
                    cardUseID = i
                if cardUse in data[i]['name']:
                    cardAttackID = i
            global interactCardListID
            for i in range(len(player1)):
                if cardUse in player1[i]['name']:
                        useCardListID = i
            for i in range(len(player2)):
                if cardInteract in player2[i]['name']:
                    interactCardListID = i
            while manaCheck == "no":
                if special == 'Y':
                    if player1[useCardListID]['special ability cost'] <= player1Mana:
                        player1Mana -= player1[useCardListID]['special ability cost']
                        manaCheck = 'yes'
                        playerSet = 'Y'
                    else:
                        tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ")
                    if tryAgain == 'N':
                        special = 'N'
                        manaCheck = 'yes'
                    else:
                        manaCheck = 'yes'
                else:
                    manaCheck = 'yes'
                    playerSet = 'Y'

        if special == 'Y':
            specialAttackDmg = data[cardUseID]['special ability damage']
            interactCardHP = player2[interactCardListID]['hp'] - specialAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP
            if player2[interactCardListID]['hp'] < 1:
                print('\n',player2[interactCardListID]['name'],'has died \n')
                del (player2[interactCardListID])
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
                print('\n',player2[interactCardListID]['name'],'has died \n')
                del (player2[interactCardListID])
                print("player 2's cards are now:\n")
                if player1 == []:
                    print("All dead")
                for i in range(len(player2)):
                    print(player2[i],'\n')
            else:
                print('\n',player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp \n')
            if player2 == []:
                global playerCards
                playerCards = 'Dead'
                print("Player 1 has won the match!")

    def player2turn(self):
        global player2Mana
        player2Mana += 2
        print("Player 2's turn!\n")
        print("\nYour cards:\n")
        for i in range(len(player2)):
            print(player2[i],'\n')
        print("You have",player2Mana,"mana \n")
        playerSet = 'no'
        while playerSet == 'no':
            tryAgain = 'test'
            playerSet = 'no'
            manaCheck = "no"
            cardUse = input("State the name of the card you'd like to use: ")
            global special
            special = input("State whether you'd like to use your card's special ability (Y/N): ")
            cardInteract = input("State the name of the card you'd like to interact with: ")
            for i in range(length):
                if cardUse in data[i]['name']:
                    cardUseID = i
                if cardUse in data[i]['name']:
                    cardAttackID = i
            global interactCardListID
            for i in range(len(player1)):
                if cardInteract in player1[i]['name']:
                    interactCardListID = i
            for i in range(len(player2)):
                if cardUse in player2[i]['name']:
                    useCardListID = i
            while manaCheck == "no":
                if special == 'Y':
                    if player2[useCardListID]['special ability cost'] <= player2Mana:
                        player2Mana -= player2[useCardListID]['special ability cost']
                        manaCheck = 'yes'
                        playerSet = 'Y'
                    else:
                        tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ")
                    if tryAgain == 'N':
                        special = 'N'
                        manaCheck = 'yes'
                    else:
                        manaCheck = 'yes'
                else:
                    playerSet = 'Y'
                    manaCheck = 'yes'

        if special == 'Y':
            specialAttackDmg = data[cardUseID]['special ability damage']
            interactCardHP = player1[interactCardListID]['hp'] - specialAttackDmg
            player1[interactCardListID]['hp'] = interactCardHP
            if player1[interactCardListID]['hp'] < 1:
                print('\n',player1[interactCardListID]['name'],'has died \n')
                del (player1[interactCardListID])
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
                print('\n',player1[interactCardListID]['name'],'has died \n')
                del (player1[interactCardListID])
                print("player 1's cards are now:\n")
                if player1 == []:
                    print("All dead")
                for i in range(len(player1)):
                    print(player1[i],'\n')
            else:
                print('\n',player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp \n')
        if player1 == []:
            global playerCards
            playerCards = 'Dead'
            print("Player 2 has won the match!")

playerturn = playerTurns()   


while playerCards == 'Alive':
    if firstPlayer == 1:
        playerturn.player1turn()
        playerturn.player2turn()
    else:
        playerturn.player2turn()
        playerturn.player1turn()