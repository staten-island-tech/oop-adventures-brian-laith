import json
import random




class playerTurns():
    def __init__(self):
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
        newCardListID = 0
        self.useCardListID = 0
        interactCardListID = 0
        specialAtttackDmg = 0
        firstPlayer = random.randint(1,2)
        playerCards = 'Alive'
        player1Mana = 0
        player2Mana = 0
        manaCheck = "no"
        playerSet = 'no'
        tryAgain = 'test'
        special = 'test'
        deathListNames = []
        specialSet = 'no'
        counter = 0
        typo1 = 'Yes'
        typo2 = 'Yes'
        typo3 = 'Yes'
        deathListNames = []
        specialSet = 'no'
        player1Mana += 2
        counter = 0
        print("Player 1's turn!\n")
        print("\nYour cards:\n")
        for player in player1:
            print(player, '\n')
        print("You have",player1Mana,"mana \n")
        playerSet = 'no'
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
                                self.useCardListID = i
                        if player1[self.useCardListID]['ability type'] == 'self heal' or player1[self.useCardListID]['ability type'] == 'mass heal' or player1[self.useCardListID]['ability type'] == 'aoe':
                            interact = "N"
                            while manaCheck == "no":
                                if player1[self.useCardListID]['special ability cost'] <= player1Mana:
                                    player1Mana -= player1[self.useCardListID]['special ability cost']
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
                        if player1[self.useCardListID]['ability type'] == 'attack' or player1[self.useCardListID]['ability type'] == 'single heal':
                            specialSet = 'Y'
                    else:
                        specialSet = 'Y'
            if interact == "Y":
                for i in range(length):
                    if cardUse in data[i]['name']:
                        cardUseID = i
                cardInteract = input("State the name of the card you'd like to interact with: ").title()
                if data[cardUseID]['ability type'] == 'single heal' and special == 'Y':
                    for i in range(len(player1)):
                        if cardInteract in player1[i]['name']:
                            typo3 = 'No'
                else:
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            typo3 = 'No'
                if typo3 == "Yes":
                    print("Uh oh someoneeeeeee made a typoooooooooo \nPlease try again:\n")
                if typo3 == 'No':
                    for i in range(len(player1)):
                        if cardUse in player1[i]['name']:
                                self.useCardListID = i
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            interactCardListID = i
                    while manaCheck == "no":
                        if special == 'Y':
                            if player1[self.useCardListID]['special ability cost'] <= player1Mana:
                                player1Mana -= player1[self.useCardListID]['special ability cost']
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
        
        #THIS STARTS THE ATTACK/INTERACT FUNCTIONS

    def otherstuff():
        if special == 'Y':
            if player1[self.useCardListID]['ability type'] == 'self heal':
                player1[self.useCardListID]['hp'] += player1[self.useCardListID]['special ability damage']
                print(player1[self.useCardListID]['name'],'is at',player1[self.useCardListID]['hp'],'hp \n')
            elif player1[self.useCardListID]['ability type'] == 'mass heal':
                for i in range(len(player1)):
                    player1[i]['hp'] += player1[self.useCardListID]['special ability damage']
                    print(player1[i]['name'],'is at',player1[i]['hp'],'hp \n')
            elif player1[self.useCardListID]['ability type'] == 'single heal':
                for i in range(len(player1)):
                    if cardInteract in player1[i]['name']:
                        interactCardListID = i
                #this adds the hp to the cards
                player1[interactCardListID]['hp'] += player1[self.useCardListID]['special ability damage']
                print(player1[interactCardListID]['name'],'is at',player1[interactCardListID]['hp'],'hp \n')
            #this is for the aoe special ability
            elif player1[self.useCardListID]['ability type'] == 'aoe':
                #damage function
                for i in range(len(player2)):
                    player2[i]['hp'] -= player1[self.useCardListID]['special ability damage']
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

