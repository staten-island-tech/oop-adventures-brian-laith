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


class playerTurns():
    def player1turn(self):
        #define variables
        deathListNames = []
        specialSet = 'no'
        global player1Mana
        player1Mana += 2
        counter = 0
        print("Player 1's turn!\n")
        print("\nYour cards:\n")
        for i in range(len(player1)):
            print(player1[i],'\n')
        print("You have",player1Mana,"mana \n")
        playerSet = 'no'
        while playerSet == 'no':
            #reset variables
            tryAgain = 'test'
            playerSet = 'no'
            specialSet = 'no'
            manaCheck = "no"
            interact = "Y"
            while specialSet == 'no':
                #reset variables
                tryAgain = 'test'
                playerSet = 'no'
                specialSet = 'no'
                manaCheck = "no"
                interact = 'Y'
                typo1 = 'Yes'
                typo2 = 'Yes'
                typo3 = 'Yes'
                #use card and ability
                cardUse = input("State the name of the card you'd like to use: ").title()
                global special
                special = input("State whether you'd like to use your card's special ability (Y/N): ").upper()
                #check for typos
                for i in range(len(player1)):
                    if cardUse in player1[i]['name']:
                        typo1 = 'No'
                    if special == 'Y' or special == 'N':
                        typo2 = 'No'
                if typo1 == "Yes" or typo2 == 'Yes':
                    print("Uh oh someoneeeeeee made a typoooooooooo \nPlease try again:\n")
                #if no typos run this
                if typo1 == 'No' and typo2 == 'No':
                    #if they wanna use their special, this will check for individual abilities to see if it needs to select a card or not
                    if special == 'Y':
                        #this sets the number in the json where the card is
                        for i in range(length):
                            if cardUse in data[i]['name']:
                                cardUseID = i
                        #this sets the number in the player list where the card is
                        for i in range(len(player1)):
                            if cardUse in player1[i]['name']:
                                useCardListID = i
                        #this checks if its ability is one that doesnt need to attack a specific card (ex. aoe, self heal, mass heal)
                        if player1[useCardListID]['ability type'] == 'self heal' or player1[useCardListID]['ability type'] == 'mass heal' or player1[useCardListID]['ability type'] == 'aoe':
                            interact = "N"
                            while manaCheck == "no":
                                #checking to see if the player has enough mana to use the ability
                                if player1[useCardListID]['special ability cost'] <= player1Mana:
                                    player1Mana -= player1[useCardListID]['special ability cost']
                                    manaCheck = 'yes'
                                    specialSet = 'Y'
                                    playerSet = 'Y'
                                else:
                                    #if they want to try again the variables wont be changed causing the "while specialSet == 'no':" loop to run again
                                    tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ").upper()
                                #if they dont wanna try again their special gets switched to N so they use their normal attack and the varables are updated 
                                #so the loops break and they can choose the card they wanna interact with as if they chose not to use their special
                                if tryAgain == 'N':
                                    special = 'N'
                                    manaCheck = 'yes'
                                    specialSet = 'Y'
                                    playerSet = 'Y'
                                else:
                                    #this is if they do wanna try again it will only exit them from the manaCheck while loop
                                    manaCheck = 'yes'
                        #this checks if its ability is one that does need to attack a specific card (ex. attack or single heal)
                        if player1[useCardListID]['ability type'] == 'attack' or player1[useCardListID]['ability type'] == 'single heal':
                            #this allows them to exit the loop but still need to go through the card interact section
                            specialSet = 'Y'
                    else:
                        #this is if they just dont wanna use their ability so it will just exit them from the loop and send them to the card interact section
                        specialSet = 'Y'
            #this is to run only if the card needs to interact with another card
            if interact == "Y":
                #this sets the number in the json where the card is
                for i in range(length):
                    if cardUse in data[i]['name']:
                        cardUseID = i
                cardInteract = input("State the name of the card you'd like to interact with: ").title()
                #this code typos in the card they wanna interact with ONLY FOR SINGLE HEAL (this is only for single heal because the card they wanna interact with is in their own deck)
                if data[cardUseID]['ability type'] == 'single heal' and special == 'Y':
                    for i in range(len(player1)):
                        if cardInteract in player1[i]['name']:
                            typo3 = 'No'
                else:
                    #this will checks for typos in the card they wanna interact with (this is for everything else since the card they wanna interact with is in the other player's deck)
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            typo3 = 'No'
                if typo3 == "Yes":
                    print("Uh oh someoneeeeeee made a typoooooooooo \nPlease try again:\n")
                #if they dont have a typo run the code
                if typo3 == 'No':
                    #this code runs to find the spot in the current player's list where the card they wanna use is
                    for i in range(len(player1)):
                        if cardUse in player1[i]['name']:
                                useCardListID = i
                    #this code runs to find the spot in the other player's list where the card they interact with is
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            interactCardListID = i
                    while manaCheck == "no":
                        #this checks to see if they have enough mana to use their ability
                        if special == 'Y':
                            if player1[useCardListID]['special ability cost'] <= player1Mana:
                                player1Mana -= player1[useCardListID]['special ability cost']
                                manaCheck = 'yes'
                                playerSet = 'Y'
                            else:
                                tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ").upper()
                            #if they dont wanna try again their special gets switched to N so they use their normal attack
                            if tryAgain == 'N':
                                special = 'N'
                                manaCheck = 'yes'
                                playerSet = 'Y'
                            else:
                                manaCheck = 'yes'
                        else:
                            #if they dont wanna use their special everything is defaulted to yes so they exit the loops
                            manaCheck = 'yes'
                            playerSet = 'Y'
        
        #THIS STARTS THE ATTACK/INTERACT FUNCTIONS

        #if they wanna use their special it runs this code
        if special == 'Y':
            #this is for the self heal special ability
            if player1[useCardListID]['ability type'] == 'self heal':
                #this adds hp to the card itself using its special ability damage (really the amount of hp it heals)
                player1[useCardListID]['hp'] += player1[useCardListID]['special ability damage']
                print(player1[useCardListID]['name'],'is at',player1[useCardListID]['hp'],'hp \n')
            #this is for the mass heal special ability
            elif player1[useCardListID]['ability type'] == 'mass heal':
                #this adds hp to the player's own deck using the card's special ability damage (really the amount of hp it heals)
                for i in range(len(player1)):
                    player1[i]['hp'] += player1[useCardListID]['special ability damage']
                    print(player1[i]['name'],'is at',player1[i]['hp'],'hp \n')
            #this is for the single heal special ability
            elif player1[useCardListID]['ability type'] == 'single heal':
                #this gets the list number for the card being healed
                for i in range(len(player1)):
                    if cardInteract in player1[i]['name']:
                        interactCardListID = i
                #this adds the hp to the cards
                player1[interactCardListID]['hp'] += player1[useCardListID]['special ability damage']
                print(player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp \n')
            #this is for the aoe special ability
            elif player1[useCardListID]['ability type'] == 'aoe':
                #damage function
                for i in range(len(player2)):
                    player2[i]['hp'] -= player1[useCardListID]['special ability damage']
                #death function
                for i in range(len(player2)):
                    if player2[i]['hp'] < 1:
                        #print deaths
                        print('\n',player2[i]['name'],'has died \n')
                        #add the names of the dead cards to a list
                        deathListNames.append(player2[i]['name'])
                #dead card removing function
                if deathListNames != []:
                    #while cards still havent been removed 
                    while deathListNames != []: 
                        counter = 0 
                        for i in range(len(player2)):
                            if deathListNames != []:
                                #this checks if the first card in the dead name list is exual to each card in the player deck
                                if deathListNames[0] == player2[counter]['name']: 
                                    #if it is, it deletes that card from both lists
                                    deathListNames.pop(0) 
                                    player2.pop(counter)
                                else:  
                                    #if it isnt, it adds one to the counter so it tests the next card
                                    counter += 1
                #it then prints the hp of the cards alive
                for i in range(len(player2)):
                    print(player2[i]['name'],'is at',player2[i]['hp'],'hp \n')
            else:
                #this does the normal attack special
                specialAttackDmg = data[cardUseID]['special ability damage']
                interactCardHP = player2[interactCardListID]['hp'] - specialAttackDmg
                player2[interactCardListID]['hp'] = interactCardHP
                #this is if the card died
                if player2[interactCardListID]['hp'] < 1:
                    print('\n',player2[interactCardListID]['name'],'has died \n')
                    del (player2[interactCardListID])
                else:
                    #this prints the damaged card's hp
                    print(player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp')
        #this is just the normal attack
        else:
            #this finds the spot in the json of the card being used
            for i in range(length):
                if cardUse in data[i]['name']:
                    cardUseID = i
            #this sets the damage and changed the hp of the attacked card
            normalAttackDmg = data[cardUseID]['damage']
            interactCardHP = player2[interactCardListID]['hp'] - normalAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP
            #this is the death function
            if player2[interactCardListID]['hp'] < 1:
                print('\n',player2[interactCardListID]['name'],'has died \n')
                del (player2[interactCardListID])
            else:
                #this will print the hp of the damaged card
                print('\n',player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp \n')
        #this checks if the player ran out of cards, ending the game (win function)
        if player2 == []:
            global playerCards
            playerCards = 'Dead'
            print("Player 1 has won the match!")
            return playerCards

    def player2turn(self):
        global player2Mana
        player2Mana += 2
        deathListNames = []
        specialSet = 'no'
        counter = 0
        print("Player 2's turn!\n")
        print("\nYour cards:\n")
        for i in range(len(player2)):
            print(player2[i],'\n')
        print("You have",player2Mana,"mana \n")
        playerSet = 'no'
        interact = "Y"
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
                typo1 = 'Yes'
                typo2 = 'Yes'
                typo3 = 'Yes'
                cardUse = input("State the name of the card you'd like to use: ").title()
                global special
                special = input("State whether you'd like to use your card's special ability (Y/N): ").upper()
                for i in range(len(player2)):
                    if cardUse in player2[i]['name']:
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
                        for i in range(len(player2)):
                            if cardUse in player2[i]['name']:
                                useCardListID = i
                        if player2[useCardListID]['ability type'] == 'self heal' or player2[useCardListID]['ability type'] == 'mass heal':
                            interact = "N"
                            while manaCheck == "no":
                                if player2[useCardListID]['special ability cost'] <= player2Mana:
                                    player2Mana -= player2[useCardListID]['special ability cost']
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
                        if player2[useCardListID]['ability type'] == 'aoe':
                            interact = "N"
                            while manaCheck == "no":
                                if player2[useCardListID]['special ability cost'] <= player2Mana:
                                    player2Mana -= player2[useCardListID]['special ability cost']
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
                        if player2[useCardListID]['ability type'] == 'attack' or player2[useCardListID]['ability type'] == 'single heal':
                            specialSet = 'Y'
                    else:
                        specialSet = 'Y'
                    if special == 'N':
                        specialSet = 'Y'
            if interact == "Y":
                for i in range(length):
                    if cardUse in data[i]['name']:
                        cardUseID = i
                cardInteract = input("State the name of the card you'd like to interact with: ").title()
                if data[cardUseID]['ability type'] == 'single heal' and special == 'Y':
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            typo3 = 'No'
                else:
                    for i in range(len(player1)):
                        if cardInteract in player1[i]['name']:
                            typo3 = 'No'
                if typo3 == "Yes":
                    print("Uh oh someoneeeeeee made a typoooooooooo \nPlease try again:\n")
                if typo3 == 'No':
                    for i in range(length):
                        if cardUse in data[i]['name']:
                            cardUseID = i
                    global interactCardListID
                    for i in range(len(player2)):
                        if cardUse in player2[i]['name']:
                            useCardListID = i
                    for i in range(len(player1)):
                        if cardInteract in player1[i]['name']:
                            interactCardListID = i
                    while manaCheck == "no":
                        if special == 'Y':
                            if player2[useCardListID]['special ability cost'] <= player2Mana:
                                player2Mana -= player2[useCardListID]['special ability cost']
                                manaCheck = 'yes'
                                playerSet = 'Y'
                            else:
                                tryAgain = input("You cannot use your special because you're broke \nWould you like to try again (Y/N)? ").upper()
                            if tryAgain == 'N':
                                special = 'N'
                                manaCheck = 'yes'
                                playerSet = 'Y'
                            else:
                                manaCheck = 'yes'
                        else:
                            manaCheck = 'yes'
                            playerSet = 'Y'

        if special == 'Y':
            if player2[useCardListID]['ability type'] == 'self heal' or player2[useCardListID]['ability type'] == 'mass heal':
                if player2[useCardListID]['ability type'] == 'self heal':
                    player2[useCardListID]['hp'] += player2[useCardListID]['special ability damage']
                    print(player2[useCardListID]['name'],'is at',player2[useCardListID]['hp'],'hp \n')
                elif player2[useCardListID]['ability type'] == 'mass heal':
                    for i in range(len(player2)):
                        player2[i]['hp'] += player2[useCardListID]['special ability damage']
                        print(player2[i]['name'],'is at',player2[i]['hp'],'hp \n')
            elif player2[useCardListID]['ability type'] == 'single heal':
                for i in range(len(player2)):
                    if cardInteract in player2[i]['name']:
                        interactCardListID = i
                player2[interactCardListID]['hp'] += player2[useCardListID]['special ability damage']
                print(player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp \n')
            elif player2[useCardListID]['ability type'] == 'aoe':
                for i in range(len(player1)):
                    player1[i]['hp'] -= player2[useCardListID]['special ability damage']
                for i in range(len(player1)):
                    if player1[i]['hp'] < 1:
                        print('\n',player1[i]['name'],'has died \n')
                        deathListNames.append(player1[i]['name'])
                if deathListNames != []:
                    while 0 < len(deathListNames):
                        counter = 0
                        for i in range(len(player1)):
                            if deathListNames != []:
                                if deathListNames[0] == player1[counter]['name']:
                                    deathListNames.pop(0) 
                                    player1.pop(counter) 
                                else: 
                                    counter += 1 
                for i in range(len(player1)): 
                    print(player1[i]['name'],'is at',player1[i]['hp'],'hp \n') 
            else: 
                specialAttackDmg = data[cardUseID]['special ability damage'] 
                interactCardHP = player1[interactCardListID]['hp'] - specialAttackDmg
                player1[interactCardListID]['hp'] = interactCardHP
                if player1[interactCardListID]['hp'] < 1:
                    print('\n',player1[interactCardListID]['name'],'has died \n')
                    del (player1[interactCardListID])
                else:
                    print(player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp')
        else:
            #normal attack
            for i in range(length):
                if cardUse in data[i]['name']:
                    cardUseID = i
            #set and use damage
            normalAttackDmg = data[cardUseID]['damage']
            interactCardHP = player1[interactCardListID]['hp'] - normalAttackDmg
            player1[interactCardListID]['hp'] = interactCardHP
            #death function
            if player1[interactCardListID]['hp'] < 1:
                print('\n',player1[interactCardListID]['name'],'has died \n')
                del (player1[interactCardListID])
            else:
                #print hp function
                print('\n',player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp \n')
        if player1 == []:
            global playerCards
            playerCards = 'Dead'
            print("Player 2 has won the match!")
         

playerturn = playerTurns()   


while playerCards == 'Alive':
    if firstPlayer == 1:
        playerturn.player1turn()
        if playerCards =='Dead':
            break
        playerturn.player2turn()
    else:
        playerturn.player2turn()
        if playerCards =='Dead':
            break
        playerturn.player1turn()