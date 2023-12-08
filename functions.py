class Game():
    def __init__(self):
        import random
        import json
        global data
        test = open("data.json", encoding="utf8")
        data = json.load(test)
        global firstplayer
        global length
        global player1cards
        global player2cards
        global playerturn
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
    def playerturn():
        mana = 2
        play = []
        good = 0
        if playerturn == 0:
            remaining_cards = 5
            print("\nYour cards are: \n")
            while good == 0:
                for i in range(remaining_cards):
                    print(player1cards[i],'\n')
                playerinput = input("What card would you like to use?: ")
                for i in range(length):
                    if playerinput == player1cards[i]['name']:
                        play.extend([player1cards[i]])
                if not play:
                    print("You made a typo\nTry again")
                else:
                    good = 1
            specialinput = input("Would you like to use your special? Y/N: ").upper()
            if specialinput == "Y" and mana >= play['special ability cost']:
                if play['ability type'] == 'attack':
                    attacked_card = []
                    attack = input("What card would you like to interact with?: ")
                    for i in range(remaining_cards):
                        if attack in player2cards[i]['name']:
                            attacked_card.extend([player2cards[id]])
                    

game = Game()
game.playerturn