class Game():
    def __init__(self):
        import random
        import json
        remaining_cards1 = 5
        remaining_cards2 = 5
        mana1 = 2
        mana2 = 2
        player1cards = []
        player2cards = []
        test = open("data.json", encoding="utf8")
        data = json.load(test)
        length = len(data)
        self.playerturn = random.randint(0,1)
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
        if self.playerturn == 0:
            print("Player 1 goes first")
        elif self.playerturn == 1:
            print("Player 2 goes first")
        self.remaining_cards1 = remaining_cards1
        self.remaining_cards2 = remaining_cards2
        self.mana1 = mana1
        self.mana2 = mana2
        self.length = length
        self.player1cards = player1cards
        self.player2cards = player2cards
    def choosecard(self):
        if self.playerturn == 0:
            cardlistid1 = 0
            used_card = []
            good = 0
            print("\nYour cards are: \n")
            for i in range(self.remaining_cards1):
                print(self.player1cards[i],"\n")
            #typo check
            while good != 1:
                use = input("What card would you like to use?: ")
                for i in range(self.remaining_cards1):
                    if use in self.player1cards[i]['name']:
                        used_card.extend([self.player1cards[i]])
                        cardlistid1 = i
                if not used_card:
                    print("No results found\nTry again")
                else:
                    good = 1
            self.used_card = used_card
            self.cardlistid1 = cardlistid1
        if self.playerturn == 1:
            cardlistid2 = 0
            used_card = []
            good = 0
            print("\nYour cards are: \n")
            for i in range(self.remaining_cards2):
                print(self.player2cards[i],"\n")
            #typo check
            while good != 1:
                use = input("What card would you like to use?: ")
                for i in range(self.remaining_cards2):
                    if use in self.player2cards[i]['name']:
                        used_card.extend([self.player2cards[i]])
                        cardlistid2 = i
                if not used_card:
                    print("No results found\nTry again")
                else:
                    good = 1
            self.used_card = used_card
            self.cardlistid2 = cardlistid2
    def special(self):
        if self.used_card[0]['ability type'] == 'attack':
            good = 0
            attacked_card = []
            while good != 1:
                if self.playerturn == 0:
                    attack_card = input("What card would you like to interact with?: ")
                    for i in range(self.remaining_cards2):
                        if attack_card in self.player2cards[i]['name']:
                            attacked_card.extend([self.player2cards[i]])
                    if not attacked_card:
                        print("No results found\nTry again")
                    else:
                        good = 1
                elif self.playerturn == 1:
                    attack_card = input("What card would you like to interact with?: ")
                    for i in range(self.remaining_cards1):
                        if attack_card in self.player1cards[i]['name']:
                            attacked_card.extend([self.player1cards[i]])
                    if not attacked_card:
                        print("No results found\nTry again")
                    else:
                        good = 1
            if self.playerturn == 0:
                if self.player2cards[self.cardlistid2]['hp'] - self.used_card[0]['special ability damage']<= 0:
                    print(f"{self.player2cards[self.cardlistid2]['name']} has died")
                    self.remaining_cards2 -= 1
                    self.playerturn += 1
                else:
                    self.player2cards[self.cardlistid2]['hp'] -= self.used_card[0]['special ability damage']
                    print(f"{self.player2cards[self.cardlistid2]['name']} is at {self.player2cards[self.cardlistid2]['hp']} hp")
                    self.playerturn += 1
            elif self.playerturn == 1:
                if self.player1cards[self.cardlistid1]['hp'] - self.used_card[0]['special ability damage']<= 0:
                    print(f"{self.player1cards[self.cardlistid1]['name']} has died")
                    self.remaining_cards1 -= 1
                    self.playerturn -= 1
                else:
                    self.player1cards[self.cardlistid1]['hp'] -= self.used_card[0]['special ability damage']
                    print(f"{self.player1cards[self.cardlistid1]['name']} is at {self.player1cards[self.cardlistid1]['hp']} hp")
                    self.playerturn -= 1
        if self.used_card[0]['ability type'] == 'self heal':
            if self.playerturn == 0:
                self.player1cards[self.cardlistid1]['hp'] += self.used_card[0]['special ability damage']
                print(f"{self.player1cards[self.cardlistid1]['name']} is at {self.player1cards[self.cardlistid1]['hp']}")
                self.playerturn += 1
            elif self.playerturn == 1:
                self.player2cards[self.cardlistid2]['hp'] += self.used_card[0]['special ability damage']
                print(f"{self.player2cards[self.cardlistid2]['name']} is at {self.player2cards[self.cardlistid2]['hp']}")
                self.playerturn += 1