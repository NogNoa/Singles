from typing import List


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
        if recent == prisoner:
            return True
        elif (recent in opened) or (len(opened) + 1 >= tries):
            return False
        else:
            opened.append(recent)


if __name__ == "__main__":
    def main(num=100):
        boxi = shuffled_boxes(num)
        for prisoner in range(100):
            if not search_boxes(prisoner, boxi, num // 2):
                print(f"Prisoner {prisoner} failed to find his number")
                break
            else:
                print(f"prisoner {prisoner} found his number")
    main()