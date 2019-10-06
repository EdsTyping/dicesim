import random
import sys


def dice_roll():
    """Begins the rolling."""
    number_to_roll = int(input("How many dice do you want to roll (Max 5)? "))
    if number_to_roll > 5 or number_to_roll <= 0:
        print("Cannot roll that many dice.")
        sys.exit()
    else:
        pass

    x = number_to_roll

    outcome = []

    for rolls in range(1, x+1):
        dice_side = random.randint(1, 6)
        outcome.append(dice_side)

    dice1 = """
       +-------+
       |       |
       |   o   |
       |       |
       +-------+"""
    dice2 = """
       +-------+
       |     o |
       |       |
       | o     |
       +-------+"""
    dice3 = """
       +-------+
       |     o |
       |   o   |
       | o     |
       +-------+"""
    dice4 = """
       +-------+
       | o   o |
       |       |
       | o   o |
       +-------+"""
    dice5 = """
       +-------+
       | o   o |
       |   o   |
       | o   o |
       +-------+"""
    dice6 = """
       +-------+
       | o   o |
       | o   o |
       | o   o |
       +-------+"""

    truesetting = True
    while truesetting:
        for roll in outcome:
            if 1 in outcome:
                print(dice1)
                outcome.remove(1)
                if outcome == []:
                    truesetting = False
                    break
                else:
                    continue
            if 2 in outcome:
                print(dice2)
                outcome.remove(2)
                if outcome == []:
                    truesetting = False
                    break
                else:
                    continue
            if 3 in outcome:
                print(dice3)
                outcome.remove(3)
                if outcome == []:
                    truesetting = False
                    break
                else:
                    continue
            if 4 in outcome:
                print(dice4)
                outcome.remove(4)
                if outcome == []:
                    truesetting = False
                    break
                else:
                    continue
            if 5 in outcome:
                print(dice5)
                outcome.remove(5)
                if outcome == []:
                    truesetting = False
                    break
                else:
                    continue
            if 6 in outcome:
                print(dice6)
                outcome.remove(6)
                if outcome == []:
                    truesetting = False
                    break
                else:
                    continue
    replay = input("Press 'Enter' to roll again. Enter 'q' to quit.")
    if replay == '':
        dice_roll()
    else:
        sys.exit()


dice_roll()
