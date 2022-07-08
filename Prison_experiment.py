from typing import List
from fractions import Fraction

def shuffled_boxes(num):
    import random
    boxi = [i for i in range(num)]
    random.shuffle(boxi)
    return boxi


def search_boxes(prisoner: int, boxi: List[int], tries: int):
    to_open = prisoner
    opened = []
    while True:
        recent = boxi[to_open]
        opened.append(recent)
        if recent == prisoner:
            return True, opened
        elif (recent in opened[:-1]) or (len(opened) >= tries):
            return False, opened
        else:
            to_open = recent


if __name__ == "__main__":
    def game(num=100, verbose=True):
        boxi = shuffled_boxes(num)
        for prisoner in range(num):
            success, opened = search_boxes(prisoner, boxi, num // 2)
            if success:
                if verbose: print(f"prisoner {prisoner} found his number, after checking: \n\t{opened}")
            else:
                if verbose: print(f"Prisoner {prisoner} failed to find his number, after checking: \n\t{opened}")
                return False
        else:
            if verbose: print("All prisoners found their number!")
            return True


    def main(runs=1024, verbose=True):
        successes = 0
        for run in range(runs):
            if game(verbose=False):
                successes += 1
        ratio = successes / runs
        print(f"{successes} out of {runs}.\t{ratio:.2%} \t{Fraction(ratio)}")


    main()
