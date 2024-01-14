import json
import random




class playerTurns():
    def __init__(self):
        test = open("data.json", encoding="utf8")
        data = json.load(test)


        self.player1 = []
        player2 = []
        length = len(data)


        rand1 = random.sample(range(length-1), 5)
        rand2 = random.sample(range(length-1), 5)
        for i in range(5):
            self.player1.extend([data[rand1[i]]])

        for i in range(5):
            player2.extend([data[rand2[i]]])

        print("\nPlayer 1's cards:\n")
        for i in range(5):
            print(self.player1[i],'\n')

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
        self.player1Mana = 0
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
        self.player1Mana += 2
        counter = 0
        print("Player 1's turn!\n")
        print("\nYour cards:\n")
        for player in self.player1:
            print(player, '\n')
        print("You have",self.player1Mana,"mana \n")
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

                for i in range(len(self.player1)):
                    if cardUse in self.player1[i]['name']:
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
                        for i in range(len(self.player1)):
                            if cardUse in self.player1[i]['name']:
                                self.useCardListID = i
                        if self.player1[self.useCardListID]['ability type'] == 'self heal' or self.player1[self.useCardListID]['ability type'] == 'mass heal' or self.player1[self.useCardListID]['ability type'] == 'aoe':
                            interact = "N"
                            while manaCheck == "no":
                                if self.player1[self.useCardListID]['special ability cost'] <= self.player1Mana:
                                    self.player1Mana -= self.player1[self.useCardListID]['special ability cost']
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
                        if self.player1[self.useCardListID]['ability type'] == 'attack' or self.player1[self.useCardListID]['ability type'] == 'single heal':
                            specialSet = 'Y'
                    else:
                        specialSet = 'Y'
            if interact == "Y":
                for i in range(length):
                    if cardUse in data[i]['name']:
                        cardUseID = i
                cardInteract = input("State the name of the card you'd like to interact with: ").title()
                if data[cardUseID]['ability type'] == 'single heal' and special == 'Y':
                    for i in range(len(self.player1)):
                        if cardInteract in self.player1[i]['name']:
                            typo3 = 'No'
                else:
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            typo3 = 'No'
                if typo3 == "Yes":
                    print("Uh oh someoneeeeeee made a typoooooooooo \nPlease try again:\n")
                if typo3 == 'No':
                    for i in range(len(self.player1)):
                        if cardUse in self.player1[i]['name']:
                                self.useCardListID = i
                    for i in range(len(player2)):
                        if cardInteract in player2[i]['name']:
                            interactCardListID = i
                    while manaCheck == "no":
                        if special == 'Y':
                            if self.player1[self.useCardListID]['special ability cost'] <= self.player1Mana:
                                self.player1Mana -= self.player1[self.useCardListID]['special ability cost']
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

    def otherstuff(self):
        if special == 'Y':
            if self.player1[self.useCardListID]['ability type'] == 'self heal':
                self.player1[self.useCardListID]['hp'] += self.player1[self.useCardListID]['special ability damage']
                print(self.player1[self.useCardListID]['name'],'is at',self.player1[self.useCardListID]['hp'],'hp \n')
            elif self.player1[self.useCardListID]['ability type'] == 'mass heal':
                for i in range(len(self.player1)):
                    self.player1[i]['hp'] += self.player1[self.useCardListID]['special ability damage']
                    print(self.player1[i]['name'],'is at',self.player1[i]['hp'],'hp \n')
            elif self.player1[self.useCardListID]['ability type'] == 'single heal':
                for i in range(len(self.player1)):
                    if cardInteract in self.player1[i]['name']:
                        interactCardListID = i
                self.player1[interactCardListID]['hp'] += self.player1[self.useCardListID]['special ability damage']
                print(self.player1[interactCardListID]['name'],'is at',self.player1[interactCardListID]['hp'],'hp \n')
            elif self.player1[self.useCardListID]['ability type'] == 'aoe':
                for i in range(len(player2)):
                    player2[i]['hp'] -= self.player1[self.useCardListID]['special ability damage']
                for i in range(len(player2)):
                    if player2[i]['hp'] < 1:
                        print('\n',player2[i]['name'],'has died \n')
                        deathListNames.append(player2[i]['name'])
                if deathListNames != []:
                    while deathListNames != []: 
                        counter = 0 
                        for i in range(len(player2)):
                            if deathListNames != []:
                                if deathListNames[0] == player2[counter]['name']: 
                                    deathListNames.pop(0) 
                                    player2.pop(counter)
                                else:  
                                    counter += 1
                for i in range(len(player2)):
                    print(player2[i]['name'],'is at',player2[i]['hp'],'hp \n')
            else:
                specialAttackDmg = data[cardUseID]['special ability damage']
                interactCardHP = player2[interactCardListID]['hp'] - specialAttackDmg
                player2[interactCardListID]['hp'] = interactCardHP
                if player2[interactCardListID]['hp'] < 1:
                    print('\n',player2[interactCardListID]['name'],'has died \n')
                    del (player2[interactCardListID])
                else:
                    print(player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp')
        else:
            for i in range(length):
                if cardUse in data[i]['name']:
                    cardUseID = i
            normalAttackDmg = data[cardUseID]['damage']
            interactCardHP = player2[interactCardListID]['hp'] - normalAttackDmg
            player2[interactCardListID]['hp'] = interactCardHP
            if player2[interactCardListID]['hp'] < 1:
                print('\n',player2[interactCardListID]['name'],'has died \n')
                del (player2[interactCardListID])
            else:
                print('\n',player2[interactCardListID]['name'],'is at',player2[interactCardListID]['hp'],'hp \n')
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

