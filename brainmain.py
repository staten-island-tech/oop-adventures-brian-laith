from functions import Game
import json
test = open("data.json", encoding="utf8")
data = json.load(test)

game = Game()
game.normal_attack()