import random


def bet(pot) -> int:
    roll = random.random()
    back = 0
    if roll > .5:
        back += pot
    elif roll < .5:
        back -= pot
    return back


def gamble(pocket: int, goal: int, length):
    pot = strat2(pocket, goal, length)
    pocket += bet(pot)
    return pocket


def strat1(pocket: int, goal: int, *args):
    return min((goal - pocket) // 10, pocket)


def strat2(pocket: int, goal: int, length: int):
    return min((goal - pocket) // 10 * (1 + length // 10), pocket)


def game(goal: int):
    pocket = 1000
    i = 0
    while 0 <= pocket < (goal - 10) and i < 550:
        pocket = gamble(pocket, goal, i)
        i += 1
    return i, pocket


def main():
    num = 100
    lens, result, jackpots = 0, 0, 0
    for _ in range(num):
        l, j = game(2000)
        r = j > 0
        lens += l
        result += r
        jackpots += j
    lens = lens / num
    result = result / num
    jackpots = jackpots / num
    print('length: ', lens, '\nwin:', result, "\njackpot", jackpots)


main()
