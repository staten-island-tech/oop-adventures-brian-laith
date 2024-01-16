from functions import Game
import json
test = open("data.json", encoding="utf8")
data = json.load(test)


game = Game()

#The game will continuously run untill one player runs out of cards 
while True:
    mana1 = game.mana1
    mana2 = game.mana2
    playerturn = game.playerturn
    game.choosecard()
    used_card = game.used_card
    ability_type = used_card[0]['ability type']
    special_ability = input("Would you like to use your special ability? Y/N: ").upper()

    #Extremely self explanatory. It's just checks for ability type and uses the corresponding function

    if playerturn%2 == 0 and mana1 >= used_card[0]['special ability cost'] and special_ability == "Y":
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

    elif playerturn%2 == 1 and mana2 >= used_card[0]['special ability cost'] and special_ability == "Y":
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

    #Too broke defaults to normal attack

    elif playerturn%2 == 0 and mana1 < used_card[0]['special ability cost'] and special_ability == "Y":
        print("You're too broke, using normal attack")
        game.normal_attack()

    elif playerturn%2 == 1 and mana2 < used_card[0]['special ability cost'] and special_ability == "Y":
        print("You're too broke, using normal attack")
        game.normal_attack()

    #Normal attack

    elif playerturn%2 == 0 and special_ability == "N":
        game.normal_attack()

    elif playerturn%2 == 1 and special_ability == "N":
        game.normal_attack()
    
    #Remaining cards get transfered after all attacks to prevent second turn win bug
    remaining_cards1 = game.remaining_cards1
    remaining_cards2 = game.remaining_cards2

    if remaining_cards1 == 0 or remaining_cards2 == 0:
        break
        
if remaining_cards1 == 0:
    print("\nPlayer 2 has won the game!!!!")
elif remaining_cards2 == 0:
    print("\nPlayer 1 has won the game!!!!")