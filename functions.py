global remaining_cards1
remaining_cards1 = []
global remaining_cards2
remaining_cards2 = []
global mana1
mana1 = 2
global mana2
mana2 = 2
global length
length = 'fill'
global player1cards
player1cards = []
global player2cards
player2cards = []
global playerturn
playerturn = 0
global cardlistid1
cardlistid1 = 0
global cardlistid2
cardlistid2 = 0
global used_card
used_card = []


remaining_cards1 = 5
remaining_cards2 = 5
mana1 = 2
mana2 = 2

class Game():
    def __init__(self):
        import random
        import json
        test = open("data.json", encoding="utf8")
        data = json.load(test)
        player1cards = []
        player2cards = []
        length = len(data)
        playerturn = random.randint(0,1)
        card1 = random.sample(range(length-1), 10)
        card2 = random.sample(range(length-1), 10)
        for i in range(5):
            player1cards.extend([data[card1[i]]])
        for i in range(5):
            player2cards.extend([data[card2[i]]])
        print("\nPlayer 1's cards:\n")
        for i in range(5):
            print(player1cards[i],'\n')
        print("\nPlayer 2's cards:\n")
        for i in range(5):
            print(player2cards[i],'\n')
        if playerturn == 0:
            print("Player 1 goes first")
        elif playerturn == 1:
            print("Player 2 goes first")
    def choosecard(self):
        cardlistid1 = 0
        cardlistid2 = 0
        if playerturn == 0:
            print(player1cards)
            used_card = []
            good = 0
            print("\nYour cards are: \n")
            for i in range(remaining_cards1):
                print(player1cards[i],"\n")
            #typo check
            while good != 1:
                use = input("What card would you like to use?: ")
                for i in range(remaining_cards1):
                    if use in player1cards[i]['name']:
                        used_card.extend([player1cards[i]])
                        cardlistid1 = i
                if not used_card:
                    print("No results found\nTry again")
                else:
                    good = 1
            used_card = used_card
        if playerturn == 1:
            used_card = []
            good = 0
            print("\nYour cards are: \n")
            for i in range(remaining_cards2):
                print(player2cards[i],"\n")
            #typo check
            while good != 1:
                use = input("What card would you like to use?: ")
                for i in range(remaining_cards2):
                    if use in player2cards[i]['name']:
                        used_card.extend([player2cards[i]])
                        cardlistid2 = i
                if not used_card:
                    print("No results found\nTry again")
                else:
                    good = 1
        used_card = used_card
        cardlistid1 = cardlistid1
        cardlistid2 = cardlistid2
    def special(self):
        mana1 = mana1
        mana2 = mana2
        if used_card[0]['ability type'] == 'attack':
            good = 0
            attacked_card = []
            while good != 1:
                if playerturn == 0:
                    attack_card = input("What card would you like to interact with?: ")
                    for i in range(remaining_cards2):
                        if attack_card in player2cards[i]['name']:
                            attacked_card.extend([player2cards[i]])
                    if not attacked_card:
                        print("No results found\nTry again")
                    else:
                        good = 1
                elif playerturn == 1:
                    attack_card = input("What card would you like to interact with?: ")
                    for i in range(remaining_cards1):
                        if attack_card in player1cards[i]['name']:
                            attacked_card.extend([player1cards[i]])
                    if not attacked_card:
                        print("No results found\nTry again")
                    else:
                        good = 1
            if playerturn == 0:
                if player2cards[cardlistid2]['hp'] - used_card[0]['special ability damage']<= 0:
                    print(f"{player2cards[cardlistid2]['name']} has died")
                    remaining_cards2 -= 1
                else:
                    player2cards[cardlistid2]['hp'] -= used_card[0]['special ability damage']
                    print(f"{player2cards[cardlistid2]['name']} is at {player2cards[cardlistid2]['hp']} hp")
            elif playerturn == 1:
                if player1cards[cardlistid1]['hp'] - used_card[0]['special ability damage']<= 0:
                    print(f"{player1cards[cardlistid1]['name']} has died")
                    remaining_cards1 -= 1
                else:
                    player1cards[cardlistid1]['hp'] -= used_card[0]['special ability damage']
                    print(f"{player1cards[cardlistid1]['name']} is at {player1cards[cardlistid1]['hp']} hp")
        if used_card[0]['ability type'] == 'self heal':
            if playerturn == 0:
                player1cards[cardlistid1]['hp'] += used_card[0]['special ability damage']
                print(f"{player1cards[cardlistid1]['name']} is at {player1cards[cardlistid1]['hp']}")
            elif playerturn == 1:
                player2cards[cardlistid2]['hp'] += used_card[0]['special ability damage']
                print(f"{player2cards[cardlistid2]['name']} is at {player2cards[cardlistid2]['hp']}")