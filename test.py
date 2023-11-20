import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)


player1 = []
player2 = []
length = len(data)


def player1turn():
    for i in range(len(player1)):
        print(player1[i], end ='\n')
    cardUse = input("State the name of the card you'd like to use: ")
    special = input("State whether you'd like to use your card's special ability (Y/N): ")
    cardInteract = (input("State the name of the card you'd like to interact with: "))
    for i in range(length):
        print(data[i])
        if data[i]["name"] == data[i][cardUse]:
            cardUseID = i
        if data[i]["name"] == data[i][cardInteract]:
            cardInteractID = i
    if special == 'Y':
        specialAttackDmg = data[i]['special ability damage']
        print(specialAttackDmg)
player1turn()

