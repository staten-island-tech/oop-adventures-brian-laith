import random
import json
from typing import List, Dict

class Game:
    def __init__(self):
       self.remaining_cards1 = 5
       self.remaining_cards2 = 5
       self.mana1 = 2
       self.mana2 = 2

       player1cards = []
       player2cards = []

       with open("data.json", encoding="utf8") as test:
           data = json.load(test)
           length = len(data)

       self.playerturn = random.randint(0,1)

       card1 = random.sample(range(length-1), 10)
       card2 = random.sample(range(length-1), 10)

       player1cards = [data[i] for i in card1[:5]]
       player2cards = [data[i] for i in card2[:5]]

       print("\nPlayer 1's cards:\n")
       for card in player1cards:
           print(card, '\n')

       print("\nPlayer 2's cards:\n")
       for card in player2cards:
           print(card, '\n')

       self.player1cards = player1cards
       self.player2cards = player2cards
       self.used_card = None

    def choosecard(self):
        selected_card_index1 = 0
        selected_card_index2 = 0
     
        if self.playerturn % 2 == 0:
           used_card = []
           print("Player 1's turn")
           print(f"\nYou have {self.mana1} mana")
           print("\nYour cards are: \n")
    
           for card in self.player1cards:
               print(card, "\n")
    
           while True:
               use = input("What card would you like to use?: ")
               for card in self.player1cards:
                   if use == card['name']:
                      used_card.append(card)
                      selected_card_index1 = card
                      break
               if not used_card:
                   print("No results found.\nTry again.")
               else:
                   break
        if self.playerturn % 2 == 1:
           used_card = []
           print("Player 2's turn")
           print(f"\nYou have {self.mana2} mana")
           print("\nYour cards are: \n")
    
           for card in self.player2cards:
               print(card, "\n")
    
           while True:
               use = input("What card would you like to use?: ")
               for card in self.player1cards:
                   if use == card['name']:
                      used_card.append(card)
                      selected_card_index2 = card
                      break
               if not used_card:
                   print("No results found.\nTry again.")
               else:
                   break
    def attack(self):
        attacked_card = []
        while True:
            try:
                if self.playerturn % 2 == 0:
                    attack_card = input("What card would you like to interact with?: ")
                    attacked_card = [card for card in self.player2cards if attack_card == card['name']]
                elif self.playerturn % 2 == 1:
                    attack_card = input("What card would you like to interact with?: ")
                    attacked_card = [card for card in self.player1cards if attack_card == card['name']]
    
                if not attacked_card:
                    raise ValueError("No results found. Try again.")
                else:
                    break
            except ValueError as e:
                print(e)
    
        if self.playerturn % 2 == 0:
            if self.player2cards[self.selected_card_index2]['hp'] - self.used_card[0]['special ability damage'] <= 0:
                print(f"{self.player2cards[self.selected_card_index2]['name']} has died")
                self.player2cards.remove(self.player2cards[self.selected_card_index2])
                self.remaining_cards2 += 1
                self.mana1 += 2
            else:
                self.player2cards[self.selected_card_index2]['hp'] -= self.used_card[0]['special ability damage']
                print(f"{self.player2cards[self.selected_card_index2]['name']} is at {self.player2cards[self.selected_card_index2]['hp']} hp")
                self.mana1 += 2
        elif self.playerturn % 2 == 1:
            if self.player1cards[self.selected_card_index1]['hp'] - self.used_card[0]['special ability damage'] <= 0:
                print(f"{self.player1cards[self.selected_card_index1]['name']} has died")
                self.player1cards.remove(self.player1cards[self.selected_card_index1])
                self.remaining_cards1 += 1
                self.mana2 += 2
            else:
                self.player1cards[self.selected_card_index1]['hp'] -= self.used_card[0]['special ability damage']
                print(f"{self.player1cards[self.selected_card_index1]['name']} is at {self.player1cards[self.selected_card_index1]['hp']} hp")
                self.mana2 += 2
    
        self.playerturn += 1
    def self_heal(self):
        if self.playerturn % 2 == 0:
            self.player1cards[self.selected_card_index1]['hp'] += self.used_card[0]['special ability damage']
            print(f"{self.player1cards[self.selected_card_index1]['name']} is at {self.player1cards[self.selected_card_index1]['hp']}")
            self.mana1 += 2
        elif self.playerturn % 2 == 1:
            self.player2cards[self.selected_card_index2]['hp'] += self.used_card[0]['special ability damage']
            print(f"{self.player2cards[self.selected_card_index2]['name']} is at {self.player2cards[self.selected_card_index2]['hp']}")
            self.mana2 += 2
        self.playerturn += 1
    def single_heal(self):
        selected_card_index1 = 0
        selected_card_index2 = 0
        if self.playerturn % 2 == 0:
            interact_card = input("What card would you like to interact with?: ")
            for index, card in enumerate(self.player1cards):
                if interact_card in card['name']:
                    self.player1cards[index]['hp'] += self.used_card[0]['special ability damage']
                    print(f"{self.player1cards[index]['name']} is at {self.player1cards[index]['hp']}")
                    self.mana1 += 2
                    return
            print("No results found.\nTry again")
        elif self.playerturn % 2 == 1:
            interact_card = input("What card would you like to interact with?: ")
            for index, card in enumerate(self.player2cards):
                if interact_card in card['name']:
                    self.player2cards[index]['hp'] += self.used_card[0]['special ability damage']
                    print(f"{self.player2cards[index]['name']} is at {self.player2cards[index]['hp']}")
                    self.mana2 += 2
                    return
            print("No results found.\nTry again")
        self.playerturn += 1
    def mass_heal(self):
        if self.playerturn % 2 == 0:
            for index, card in enumerate(self.player1cards):
                card['hp'] += self.used_card[0]['special ability damage']
                print(f"{card['name']} is at {card['hp']}")
                self.mana1 += 2
        if self.playerturn % 2 == 1:
            for index, card in enumerate(self.player2cards):
                card['hp'] += self.used_card[0]['special ability damage']
                print(f"{card['name']} is at {card['hp']}")
                self.mana2 += 2
        self.playerturn += 1
    def aoe(self):
        dead = []
        if self.playerturn % 2 == 0:
            for index, card in enumerate(self.player2cards):
                if card['hp'] - self.used_card[0]['special ability damage'] <= 0:
                    print(f"\n{card['name']} has died")
                    dead.append(card)
                else:
                    card['hp'] -= self.used_card[0]['special ability damage']
                    print(f"\n{card['name']} is at {card['hp']} hp")
            for card in dead:
                self.player2cards.remove(card)
                self.remaining_cards2 -= len(dead)
            self.mana1 += 2
        elif self.playerturn % 2 == 1:
            for index, card in enumerate(self.player1cards):
                if card['hp'] - self.used_card[0]['special ability damage'] <= 0:
                    print(f"\n{card['name']} has died")
                    dead.append(card)
                else:
                    card['hp'] -= self.used_card[0]['special ability damage']
                    print(f"\n{card['name']} is at {card['hp']} hp")
            for card in dead:
                self.player1cards.remove(card)
                self.remaining_cards1 -= len(dead)
            self.mana2 += 2
        self.playerturn += 1
    def normal_attack(self):
        good = False
        attacked_card = []

        while not good:
            try:
                if self.playerturn % 2 == 0:
                    attack_card = input("What card would you like to interact with?: ")
                    attacked_card = [card for card in self.player2cards if attack_card == card['name']]
                elif self.playerturn % 2 == 1:
                    attack_card = input("What card would you like to interact with?: ")
                    attacked_card = [card for card in self.player1cards if attack_card == card['name']]

                if not attacked_card:
                    raise ValueError("No results found. Try again.")
                else:
                    good = True
            except ValueError as e:
                print(e)

        if self.playerturn % 2 == 0:
            if self.player2cards[self.selected_card_index2]['hp'] - self.used_card[0]['damage'] <= 0:
                print(f"{self.player2cards[self.selected_card_index2]['name']} has died")
                self.player2cards.remove(self.player2cards[self.selected_card_index2])
                self.remaining_cards2 -= 1
                self.mana1 += 2
            else:
                self.player2cards[self.selected_card_index2]['hp'] -= self.used_card[0]['damage']
                print(f"{self.player2cards[self.selected_card_index2]['name']} is at {self.player2cards[self.selected_card_index2]['hp']} hp")
                self.mana1 += 2
        elif self.playerturn % 2 == 1:
            if self.player1cards[self.selected_card_index1]['hp'] - self.used_card[0]['damage'] <= 0:
                print(f"{self.player1cards[self.selected_card_index1]['name']} has died")
                self.player1cards.remove(self.player1cards[self.selected_card_index1])
                self.remaining_cards1 -= 1
                self.mana2 += 2
            else:
                self.player1cards[self.selected_card_index1]['hp'] -= self.used_card[0]['damage']
                print(f"{self.player1cards[self.selected_card_index1]['name']} is at {self.player1cards[self.selected_card_index1]['hp']} hp")
                self.mana2 += 2

        self.playerturn += 1