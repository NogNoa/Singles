import random


def gamble(pocket: int, goal: int) -> int:
    pot = (goal - pocket) // 10
    roll = random.random()
    if roll > .5:
        pocket += pot
    elif roll < .5:
        pocket -= pot
    return pocket


