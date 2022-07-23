import random

def roll_dice():
    return random.randint(1, 6)

print("Dice Roller")

while 1:
    choice = input("Press 'r' to roll the dice or 'q' to quit: ")
    if choice == 'r':
        print(roll_dice())
    elif choice == 'q':
        break
    