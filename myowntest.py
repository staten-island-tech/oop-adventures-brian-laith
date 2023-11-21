import json
import random

test = open("data.json", encoding="utf8")
data = json.load(test)


player1 = []
player2 = []
length = len(data)


rand1 = random.sample(range(length-1), 5)
rand2 = random.sample(range(length-1), 5)
for i in range(5):
    player1.extend([data[rand1[i]]])

for i in range(5):
    player2.extend([data[rand2[i]]])

print("\nPlayer one's cards:\n")
for i in range(5):
    print(player1[i],'\n')

print("\nPlayer two's cards:\n")
for i in range(5):
    print(player2[i],'\n')


first = random.randint(0,1)

class Game():
    def __init__(self):        
        if first == 0:
            print("Player 1 goes first")
        else:
            print("Player 2 goes first")
            
    def run(self):
        if first == 0:
            CardPlay = input("What card would you like to play: ")
            for i in range(5):
                if CardPlay in player1[i]['name']:
                    play = player1[i]['name']
        elif first == 1:
            CardPlay = input("What card would you like to play: ")
            for i in range(5):
                if CardPlay in player2[i]['name']:
                    play = player2[i]['name']
        try:
            play
        except NameError:
            print("No results found. Run the code again.")
            exit()
        print(play)
    
g = Game()
g.run()