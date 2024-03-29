def choose(all: int, chosen: int) -> int:
    import math
    return math.prod(range(chosen + 1, all + 1)) // math.factorial(all - chosen)  # integer division faster


def case_probability(all: int, chosen: int, single_prbb: float) -> float:
    return choose(all, chosen) * single_prbb ** chosen * (1 - single_prbb) ** (all - chosen)


def false_positive_rate(all: int, chosen: int) -> float:
    return case_probability(all, chosen, .5)


def test(accusation_treshold: float, catch_target: float, unfairness: float):
    assert (0 < unfairness <= 0.5)

    def true_positive_rate(all: int, chosen: int) -> float:
        return case_probability(all, chosen, .5 + unfairness)
    flips = 1
    while True:
        true_positives = [true_positive_rate(flips, heads) for heads in range(flips + 1)]
        false_positives = [false_positive_rate(flips, heads) for heads in range(flips + 1)]
        for heads_treshold in range(flips + 1):
            true_positives_sum = sum(true_positives[heads_treshold:])
            false_positives_sum = sum(false_positives[heads_treshold:])
            if true_positives_sum > catch_target and false_positives_sum < accusation_treshold:
                return flips, heads_treshold, true_positives_sum, false_positives_sum
        flips += 1


if __name__ == "__main__":
    def main():
        flips, heads_treshold, tps, fps = test(.05, .8, 0.25)
        print(f"Fliped {flips} coins.")
        print(f"Accused players who got {heads_treshold} or more heads.")
        print(f"Accused {fps:.2%} of fair players.")
        print(f"Catched {tps:.2%} of cheaters.")


    main()
