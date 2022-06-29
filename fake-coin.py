def choose(all: int, chosen: int) -> int:
    import math
    return math.prod(range(chosen + 1, all + 1)) // math.factorial(all - chosen)  # integer division faster


def case_probability(all: int, chosen: int, single_prbb: float) -> float:
    return choose(all, chosen) * single_prbb ** chosen * (1 - single_prbb) ** (all - chosen)


def true_positive_rate(all: int, chosen: int) -> float:
    return case_probability(all, chosen, .75)


def false_positive_rate(all: int, chosen: int) -> float:
    return case_probability(all, chosen, .5)


if __name__ == "__main__":
    accusation_treshold = .2
    catch_target = .8
    satisfied = False
    flips = 1
    while not satisfied:
        heads_treshold = 0
        tpr = true_positive_rate(flips, heads_treshold)
        if tpr > catch_target:
            fpr = false_positive_rate(flips, heads_treshold)
            if fpr < accusation_treshold:
                print(f"Fliped {flips} coins.")
                print(f"Accused players who got {heads_treshold}% or more heads.")
                print(f"Accused {int(fpr*100)}% of fair players.")
                print(f"Catched {int(tpr*100)}% of cheaters.")
                satisfied = True
            else:
                heads_treshold += 1
        else:
            flips += 1

