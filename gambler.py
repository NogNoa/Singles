import random


def bet(pot) -> int:
    roll = random.random()
    back = 0
    if roll > .5:
        back += pot
    elif roll < .5:
        back -= pot
    return back


def gamble(pocket: int, goal: int):
    pot = (goal - pocket) // 10
    pocket += bet(pot)
    return pocket


def game(goal: int):
    pocket = 1000
    i = 0
    while 0 <= pocket < goal - 10:
        pocket = gamble(pocket, goal)
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
    print('lens: ', lens, '\nresult:', result, "\njackpot", jackpots)


main()
