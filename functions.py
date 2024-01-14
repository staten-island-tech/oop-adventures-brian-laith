class Game():
    # INIT COMPLETLY FINE #
    def __init__(self):
        import random
        import json

        self.remaining_cards1 = 5
        self.remaining_cards2 = 5
        self.mana1 = 2
        self.mana2 = 2

        player1cards = []
        player2cards = []

        test = open("data.json", encoding="utf8")
        data = json.load(test)
        length = len(data)

        self.playerturn = random.randint(0,1)

        card1 = random.sample(range(length), 10)
        card2 = random.sample(range(length), 10)

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

        self.player1cards = player1cards
        self.player2cards = player2cards
        self.used_card = None
    #SHOULD BE FIXED
    def choosecard(self):
        cardlistid1 = 0
        cardlistid2 = 0

        if self.playerturn%2 == 0:
            used_card = []
            print("Player 1's turn")
            print(f"\nYou have {self.mana1} mana")
            print("\nYour cards are: \n")

            for i in self.player1cards:
                print(i,"\n")

            #typo check
            while True:
                use = input("What card would you like to use?: ")

                for card in self.player1cards:
                    if use in card['name']:
                        used_card.extend([card])
                        cardlistid1 = self.player1cards.index(card)
                if not used_card:
                    print("No results found\nTry again")
                else:
                    break
        if self.playerturn%2 == 1:
            used_card = []
            print("Player 2's turn")
            print(f"\nYou have {self.mana1} mana")
            print("\nYour cards are: \n")
            for i in self.player2cards:
                print(i,"\n")

            #typo check
            while True:
                use = input("What card would you like to use?: ")

                for card in self.player2cards:
                    if use in card['name']:
                        used_card.extend([card])
                        cardlistid2 = self.player2cards.index(card)
                if not used_card:
                    print("No results found\nTry again")
                else:
                    break

        self.used_card = used_card
        self.cardlistid1 = cardlistid1
        self.cardlistid2 = cardlistid2
    #GOOD
    def attack(self):
        attacked_card = []
        attack_id = 0
        while True:
            if self.playerturn%2 == 0:
                attack_card = input("What card would you like to interact with?: ")
                for card in self.player2cards:
                    if attack_card == card['name']:
                        attacked_card.extend([card])
                        attack_id = self.player2cards.index(card)
                if not attacked_card:
                    print("No results found\nTry again")
                else:
                    break
            elif self.playerturn%2 == 1:
                attack_card = input("What card would you like to interact with?: ")
                for card in self.player1cards:
                    if attack_card == card['name']:
                        attacked_card.extend([card])
                        attack_id = self.player1cards.index(card)
                if not attacked_card:
                    print("No results found\nTry again")
                else:
                    break
        #attack part and health subtraction
        if self.playerturn%2 == 0:

            if self.used_card[0]['special ability damage'] >= attacked_card[0]['hp']:
                print(f"{attacked_card[0]['name']} has died")
                self.player2cards.remove(attacked_card[0])
                self.remaining_cards2 -= 1
                self.mana1 += 2
                self.mana1 -= self.used_card[0]['special ability cost']
            else:
                self.player2cards[attack_id]['hp'] -= self.used_card[0]['special ability damage']
                print(f"{attacked_card[0]['name']} is at {self.player2cards[attack_id]['hp']} hp")
                self.mana1 += 2
                self.mana1 -= self.used_card[0]['special ability cost']

        elif self.playerturn%2 == 1:
            if self.used_card[0]['special ability damage'] >= attacked_card[0]['hp']:
                print(f"{attacked_card[0]['name']} has died")
                self.player1cards.remove(attacked_card[0])
                self.remaining_cards1 -= 1
                self.mana2 += 2
                self.mana2 -= self.used_card[0]['special ability cost']
            else:
                self.player1cards[attack_id]['hp'] -= self.used_card[0]['special ability damage']
                print(f"{attacked_card[0]['name']} is at {self.player1cards[attack_id]['hp']} hp")
                self.mana2 += 2
                self.mana2 -= self.used_card[0]['special ability cost']

        self.playerturn += 1
    #ALSO GOOD
    def self_heal(self):
        if self.playerturn%2 == 0:
            self.player1cards[self.cardlistid1]['hp'] += self.used_card[0]['special ability damage']
            print(f"{self.used_card[0]['name']} is at {self.player1cards[self.cardlistid1]['hp']}")
            self.mana1 += 2
            self.mana1 -= self.used_card[0]['special ability cost']
        elif self.playerturn%2 == 1:
            self.player2cards[self.cardlistid2]['hp'] += self.used_card[0]['special ability damage']
            print(f"{self.used_card[0]['name']} is at {self.player2cards[self.cardlistid2]['hp']}")
            self.mana2 += 2
            self.mana2 -= self.used_card[0]['special ability cost']
        self.playerturn += 1
    #SHOULD BE WORKING
    def single_heal(self):
        index = 0
        interact_card = []        
        if self.playerturn%2 == 0:
            user_input = input("What card would you like to interact with?: ")
            while True:
                for card in self.player1cards:
                    if card['name'] in user_input:
                        interact_card.extend([card])
                        index = self.player1cards.index[card]
                        break
                    if not interact_card:
                        print("No results found.\nTry again.")

        elif self.playerturn%2 == 1:
            user_input = input("What card would you like to interact with?: ")
            while True:
                for card in self.player2cards:
                    if card['name'] in user_input:
                        interact_card.extend([card])
                        index = self.player2cards.index[card]
                        break
                    if not interact_card:
                        print("No results found.\nTry again.")
        
        if self.playerturn%2 == 0:
            self.player1cards[index]['hp'] += self.used_card[self.cardlistid1]['special ability damage']
            print(f"{self.player1cards[index]['name']} is at {self.player1cards[index]['hp']}")
            self.mana1 += 2
            self.mana1 -= self.used_card[0]['special ability cost']

        elif self.playerturn%2 == 1:
            self.player2cards[index]['hp'] += self.used_card[self.cardlistid2]['special ability damage']
            print(f"{self.player2cards[index]['name']} is at {self.player2cards[index]['hp']}")
            self.mana2 += 2
            self.mana2 -= self.used_card[0]['special ability cost']
        

        self.playerturn += 1
    #MAYBE
    def mass_heal(self):
        if self.playerturn%2 == 0:
            for i in range(self.remaining_cards1):
                self.player1cards[i]['hp'] += self.used_card[0]['special ability damage']
                print(f"{self.player1cards[i]['name']} is at {self.player1cards[i]['hp']}")
                self.mana1 += 2
                self.mana1 -= self.used_card[0]['special ability cost']
        if self.playerturn%2 == 1:
            for i in range(self.remaining_cards2):
                self.player2cards[i]['hp'] += self.used_card[0]['special ability damage']
                print(f"{self.player2cards[i]['name']} is at {self.player2cards[i]['hp']}")
                self.mana2 += 2
                self.mana2 -= self.used_card[0]['special ability cost']
        self.playerturn += 1
    #????
    def aoe(self):
        dead = []
        if self.playerturn%2 == 0:
            for i in range(self.remaining_cards2):
                if self.player2cards[i]['hp'] - self.used_card[0]['special ability damage']<= 0:
                    print(f"\n{self.player2cards[i]['name']} has died")
                    dead.extend([self.player2cards[i]])
                else:
                    self.player2cards[i]['hp'] -= self.used_card[0]['special ability damage']
                    print(f"\n{self.player2cards[i]['name']} is at {self.player2cards[i]['hp']} hp")
            for i in dead:
                self.player2cards.remove(i)
                self.remaining_cards2 -= len(dead)
            self.mana1 += 2
            self.mana1 -= self.used_card[0]['special ability cost']
        elif self.playerturn%2 == 1:
            for i in range(self.remaining_cards1):
                if self.player1cards[i]['hp'] - self.used_card[0]['special ability damage'] <= 0:
                    print(f"\n{self.player1cards[i]['name']} has died")
                    dead.extend([self.player1cards[i]])
                else:
                    self.player1cards[i]['hp'] -= self.used_card[0]['special ability damage']
                    print(f"\n{self.player1cards[i]['name']} is at {self.player1cards[i]['hp']} hp")
            for i in dead:
                self.player1cards.remove(i)
                self.remaining_cards1 -= len(dead)
            self.mana2 += 2
            self.mana2 -= self.used_card[0]['special ability cost']
        self.playerturn += 1
    #SAME AS SPECIAL ATTACK SO IT SHOULD BE FINE
    def normal_attack(self):
        attacked_card = []
        attack_id = 0
        while True:
            if self.playerturn%2 == 0:
                attack_card = input("What card would you like to interact with?: ")
                for card in self.player2cards:
                    if attack_card == card['name']:
                        attacked_card.extend([card])
                        attack_id = self.player2cards.index(card)
                if not attacked_card:
                    print("No results found\nTry again")
                else:
                    break
            elif self.playerturn%2 == 1:
                attack_card = input("What card would you like to interact with?: ")
                for card in self.player1cards:
                    if attack_card == card['name']:
                        attacked_card.extend([card])
                        attack_id = self.player1cards.index(card)
                if not attacked_card:
                    print("No results found\nTry again")
                else:
                    break
        #attack part and health subtraction
        if self.playerturn%2 == 0:

            if self.used_card[0]['damage'] >= attacked_card[0]['hp']:
                print(f"{attacked_card[0]['name']} has died")
                self.player2cards.remove(attacked_card[0])
                self.remaining_cards2 -= 1
                self.mana1 += 2
            else:
                self.player2cards[attack_id]['hp'] -= self.used_card[0]['damage']
                print(f"{attacked_card[0]['name']} is at {self.player2cards[attack_id]['hp']} hp")
                self.mana1 += 2

        elif self.playerturn%2 == 1:
            if self.used_card[0]['damage'] >= attacked_card[0]['hp']:
                print(f"{attacked_card[0]['name']} has died")
                self.player1cards.remove(attacked_card[0])
                self.remaining_cards1 -= 1
                self.mana2 += 2
            else:
                self.player1cards[attack_id]['hp'] -= self.used_card[0]['damage']
                print(f"{attacked_card[0]['name']} is at {self.player1cards[attack_id]['hp']} hp")
                self.mana2 += 2

        self.playerturn += 1