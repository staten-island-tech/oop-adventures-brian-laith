from functions import Game
import time
import json
test = open("data.json", encoding="utf8")
data = json.load(test)


game = Game()
remaining_cards1 = game.remaining_cards1
remaining_cards2 = game.remaining_cards2

while remaining_cards1 != 0 or remaining_cards2 != 0:
    print("GRAHHHHHHHHHHHHHHH", game.remaining_cards1)
    print("GRAHHHHHHHHHHHHHHH", remaining_cards1)
    time.sleep(5)

    mana1 = game.mana1
    mana2 = game.mana2
    playerturn = game.playerturn
    game.choosecard()
    used_card = game.used_card
    ability_type = used_card[0]['ability type']
    special_ability = input("Would you like to use your special ability? Y/N: ").upper()

    if playerturn == 0 and mana1 >= used_card[0]['special ability cost'] and special_ability == "Y":
        if ability_type == "attack":
            game.attack()

        elif ability_type == "self heal":
            game.self_heal()

        elif ability_type == "single heal":
            game.single_heal()

        elif ability_type == "mass heal":
            game.mass_heal()

        elif ability_type == "aoe":
            game.aoe()

    elif playerturn == 1 and mana2 >= used_card[0]['special ability cost'] and special_ability == "Y":
        if ability_type == "attack":
            game.attack()

        elif ability_type == "self heal":
            game.self_heal()

        elif ability_type == "single heal":
            game.single_heal()

        elif ability_type == "mass heal":
            game.mass_heal()

        elif ability_type == "aoe":
            game.aoe()

    elif playerturn == 0 and mana1 < used_card[0]['special ability cost'] and special_ability == "Y":
        print("You're too broke, using normal attack")
        game.normal_attack()

    elif playerturn ==  1 and mana2 < used_card[0]['special ability cost'] and special_ability == "Y":
        print("You're too broke, using normal attack")
        game.normal_attack()

    elif playerturn == 0 and special_ability == "N":
        game.normal_attack()

    elif playerturn == 1 and special_ability == "N":
        game.normal_attack()
        
if remaining_cards1 == 0:
    print("Player 2 has won the game")
elif remaining_cards2 == 0:
    print("Player 1 has won the game")