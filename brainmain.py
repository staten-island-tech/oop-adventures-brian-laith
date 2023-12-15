from functions import Game
import json
test = open("data.json", encoding="utf8")
data = json.load(test)


game = Game()
mana1 = game.mana1
mana2 = game.mana2
playerturn = game.playerturn
game.choosecard()
used_card = game.used_card
special_ability = input("Would you like to use your special ability? Y/N: ").upper()
if playerturn == 0 and mana1 >= used_card[0]['special ability cost']:
    game.special()
elif playerturn == 1 and mana2 >= used_card[0]['special ability cost']:
    game.special()