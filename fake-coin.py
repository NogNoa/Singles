def choose(all: int, chosen: int) -> int | float:
    import math
    return math.prod(range(chosen + 1, all + 1)) / math.factorial(all - chosen)


def CaseProbability(all: int, chosen: int, single_prbb: float) -> int | float:
    return choose(all, chosen) * single_prbb ** chosen * (1 - single_prbb) ** (all - chosen)


for i in range(6):
    print(CaseProbability(5, i, .75))
