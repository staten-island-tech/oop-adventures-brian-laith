class Game():
    @classmethod
    def __init__(self):
        import random
        import json
        remaining_cards = 5
        test = open("data.json", encoding="utf8")
        data = json.load(test)
        player1cards = []
        player2cards = []
        length = len(data)
        firstplayer = random.randint(0,1)
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
        if firstplayer == 0:
            print("Player 1 goes first")
            playerturn = 0
        elif firstplayer == 1:
            print("Player 2 goes first")
            playerturn = 1
        self.length = length
        self.player1cards = player1cards
        self.player2cards = player2cards
        self.playerturn = playerturn
        self.remaining_cards = remaining_cards
        print(player1cards)
    @classmethod
    def normal_attack(self):
        print(self.player1cards)
        x = 0
        if self.playerturn == 0:
            print("Your cards are: \n")
            while x < 6:
                print(self.player1cards[x]"\n")
                x += 1