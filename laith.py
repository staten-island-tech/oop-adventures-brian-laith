import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)






class Game():
    def __init__(self): 
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

        self.cardUseID = 0
        self.newCardListID = 0
        self.useCardListID = 0
        self.interactCardListID = 0
        self.specialAtttackDmg = 0
        self.firstPlayer = random.randint(1,2)
        self.playerCards = 'Alive'
        self.player1Mana = 0
        self.player2Mana = 0
        self.manaCheck = "no"
        self.playerSet = 'no'
        self.tryAgain = 'test'
        self.special = 'test'
        self.deathListNames = []
        self.specialSet = 'no'
        self.counter = 0
        self.typo1 = 'Yes'
        self.typo2 = 'Yes'
        self.typo3 = 'Yes'
        self.currentPlayer = [player1,self.player1Mana]