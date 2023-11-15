import json
import os
more = "True"
## Create Class for creating new dictionaries here
class Card:
    def makeCard(self,name,hp,dmg,ability,abilityDmg,specialMana):
        self.name = name
        self.hp = hp
        self.dmg = dmg
        self.ability = ability
        self.abilityDmg = abilityDmg
        self.specialMana = specialMana
        card = {'name':name,'hp':hp,'damage':dmg,'special ability':ability,'special ability cost':specialMana}
        return card

again = "true"
while again == "true":
    with open("data.json", "r") as f:
        # Serialize the updated Python list to a JSON string
        data = json.load(f)
        ##Call classes in here
        card = Card()
        name = input("State the card's name: ")
        hp = int(input("State the card's HP: "))
        dmg = int(input("State the card's dmg: "))
        ability = input("State the card's ability name: ")
        abilityDmg = int(input("State the card's ability damage: "))
        specialMana = int(input("State the card's ability cost: "))
        newCard = card.makeCard(name, hp, dmg, ability, abilityDmg, specialMana)
        data.append(newCard)
        print(data)








    #No code needed below this line
    # Creates a new JSON file with the updated data
    new_file = "updated.json"
    with open(new_file, "w") as f:
        # Serialize the updated Python list to a JSON string
        json_string = json.dumps(data, indent=4)

        # Write the JSON string to the new JSON file
        f.write(json_string)

    # Overwrite the old JSON file with the new one
    os.remove("data.json")
    os.rename(new_file, "data.json")
    userMore = input("Do you want to add another card (Y/N): ")
    if userMore == "N":
        again = "false"