"""Designed and programmed by chris gaylo, syosset H.S.~~9/12/70
This so called port from early BASIC to Python by Omer Dassa ~~31/03/22

Published under a BSD open source license

Copyright (c) Omer Dassa 2020

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

Redistributions in binary form must reproduce the above copyright notice, this
list of conditions and the following disclaimer in the documentation and/or other
materials provided with the distribution.

Neither the name of the Osmosoft Limited nor the names of its contributors may be
used to endorse or promote products derived from this software without specific
prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT
SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED
TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH
DAMAGE."""


def main():
    # 110
    print(" " * 28, 'HIGH NOON\n', " " * 27, '~' * 9, '\n' * 2)
    want = input("Do you want instructions?").upper()[0]  # original: only upper case
    if not want == "N":  # original: has to be the full NO
        instruct()  # 180
    rng = rng_init()  # 460
    dist = distance_init()  # 530


def instruct():
    # 180
    print(
        "\n" * 2, 'You have been challenged to a showdown by Black Bart, one of'
                  'the meanest desperadoes west of the allegheny mountains.'
                  'While you are walking down a dusty, seserted side stree,'
                  'Black Bart emerges from a saloon one hundred paces away. By'
                  'agreement, you each have four cartridges in you six-guns.'
                  'Your marksmanship equals his. At the start of the walk, nei-'
                  'ther of you can possibly hit the other, and at the wnd of'
                  'the walk, neither can miss. The closer you get, the better'
                  "your chances of hitting bart, but he also has better chances"
                  'of hitting you.')
    want = input('Do you still want to continue?').upper()[0]
    if want == "N":
        fin(2)  # 1370
    else:
        return  # 460


def rng_init():
    # 460
    import random
    import math
    lucky = float(input("What is your lucky number for today?"))
    lucky = 1e4 * math.fabs(math.sin(lucky))
    lucky = (lucky % 1) * 1e3 // 1
    random.seed(lucky)
    return random.randint  # 530


def distance_init():
    # 530
    dist = [100]

    def distance():
        return dist[0]

    def reduce(steps=0):
        nonlocal dist
        dist[0] -= steps

    distance.reduce = reduce
    return distance


def fin(resp):
    # (,,1370)[resp]
    pass
