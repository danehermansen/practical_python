import random
from xmlrpc.server import DocCGIXMLRPCRequestHandler

def rolldice():
    dice_total = random.randint(1, 6) + random.randint(1, 6) 
    return dice_total


player1 = input("Enter your name")
player2 = input("Enter your other name")

roll1 = rolldice()
roll2 = rolldice()

print(player1, 'rolled', roll1)
print(player2, 'rolled', roll2)


if roll1 > roll2: 
    print(player1, 'wins')
elif roll1 < roll2:
    print(player2, 'wins')
elif roll1 == roll2:
    print(player1, player2, 'ties!')


