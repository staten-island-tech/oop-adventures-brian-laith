player1HP = []
player2HP = []

for i in range(length):
    if player1[0]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[1]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[2]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[3]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])
for i in range(length):
    if player1[4]['name'] in data[i]['name']:
        player1HP.append(data[i]['hp'])

for i in range(length):
    if player2[0]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[1]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[2]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[3]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])
for i in range(length):
    if player2[4]['name'] in data[i]['name']:
        player2HP.append(data[i]['hp'])