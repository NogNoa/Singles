from typing import List


def shuffled_boxes(num=100):
    import random
    boxi = [i for i in range(num)]
    random.shuffle(boxi)
    return boxi


def open_box(box: int, boxi: List[int]):
    return boxi[box]


def search_box(prisoner: int, boxi: List[int]):
    to_open = prisoner
    while True:
        recent = boxi[to_open]
