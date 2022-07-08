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
        opened.append(recent)
        if recent == prisoner:
            return True, opened
        elif (recent in opened[:-1]) or (len(opened) >= tries):
            return False, opened
        else:
            to_open = recent


if __name__ == "__main__":
    def main(num=100):
        boxi = shuffled_boxes(num)
        for prisoner in range(num):
            success, opened = search_boxes(prisoner, boxi, num // 2)
            if success:
                print(f"prisoner {prisoner} found his number, after checking: \n\t{opened}")
            else:
                print(f"Prisoner {prisoner} failed to find his number, after checking: \n\t{opened}")
                break



    main()
