# dice_roller.py
# Simulates rolling a dice

import random

def roll_dice():
    return random.randint(1, 6)

if __name__ == "__main__":
    while True:
        input("Press Enter to roll the dice 🎲 (or Ctrl+C to quit)")
        print("You rolled:", roll_dice())
