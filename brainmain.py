from functions import Game, remaining_cards1, remaining_cards2
import json
test = open("data.json", encoding="utf8")
data = json.load(test)


game = Game()
game.choosecard()
special_ability = input("Would you like to use your special ability? Y/N: ").upper()
if special_ability == "Y":
    game.special()