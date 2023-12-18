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
ability_type = used_card[0]['ability type']
special_ability = input("Would you like to use your special ability? Y/N: ").upper()
if playerturn == 0 and mana1 >= used_card[0]['special ability cost']:
    game.single_heal()
elif playerturn == 1 and mana2 >= used_card[0]['special ability cost']:
    game.single_heal()
elif playerturn == 0 and mana1 < used_card[0]['special ability cost']:
    print("You're too broke, using normal attack")
    #commits normal attack but I didn't do it yet
elif playerturn ==  1 and mana2 < used_card[0]['special ability cost']:
    print("You're too broke, using normal attack")
    #does something that laith can't do