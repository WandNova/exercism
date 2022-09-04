# Score categories.
# Change the values as you see fit.
YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    dice_set = list(set(dice))
    dice.sort()
    if category in [ONES, TWOS, THREES, FOURS, FIVES, SIXES]:
        return dice.count(category) * category
    if category == FOUR_OF_A_KIND:
        if len(dice_set) > 2 or dice.count(dice_set[0]) in [2, 3]:
            return 0
        if len(dice_set) == 1:
            return dice_set[0] * 4
        if dice.count(dice_set[0]) == 4:
            return dice_set[0] * 4
        return dice_set[1] * 4
    if category == FULL_HOUSE and len(set(dice)) == 2 and dice.count(dice_set[0]) in [2, 3]:
        return sum(dice)
    if category == LITTLE_STRAIGHT and dice == [1, 2, 3, 4, 5]:
        return 30
    if category == BIG_STRAIGHT and dice == [2, 3, 4, 5, 6]:
        return 30
    if category == CHOICE:
        return sum(dice)
    if category == YACHT and len(dice_set) == 1:
        return 50
    return 0
