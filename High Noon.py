"""Designed and programmed by chris gaylo, syosset H.S.~~9/12/70
This so called Python port by Omer Dassa ~~24/02/20
assume screen length 64 char
number comments are original basic line numbers,
as original uses goto commands"""
# from math import sin, fabs
from random import randint
from sys import exit

X: int = 100  # distance ε paces
C: int = 0  # bullets counting up to 4
P: int = 0  # Bart's bullets
T = 0
j = 0


def main():
    # 110
    global j
    print(" " * 28, 'HIGH NOON\n', " " * 27, '~' * 9, '\n' * 2)
    D = input("Do you want instructions?").upper()[0]  # original: only upper case
    if D is not "N":  # original: has to be the full NO
        instruct()
    """
    A=input("What is your lucky number for today?")
    A=float(A)
    A=10000*fabs(sin(A))
    A=(A-int(A))*1000
    for I = 1 to A
    B=rnd(0)
    next I
    R: random() #a one time randomization between 0.0 to 1.0 RND(-1)
    """
    while True:
        moves()
        bart_move()


def moves():
    # 550
    global X, C, P, j
    j = 0
    print("The moves are as follows:", '\n' * 2, ' ' * 29, '*Moves*\n', ' ' * 29, '=' * 7)
    print("1.Advance", "\t" * 3, " " * 6,
          "2.Stand Still\t3.Fire\n4.Jump Behind The Watering Trough\t5.Give Up\t6.Turn Tail And Run")
    B = int(input("What is your strategy?"))
    if B == 1:
        X = advance(X)
    elif B == 2:
        # 1390 Stand
        print("That move made you a perfect Stationary Target")
    elif B == 3:
        C = fire(C, X)
    elif B == 4:
        # 1410
        j = 1
        jump()
    elif B == 5:
        give_up()
    elif B == 6:
        run(P)
    else:
        print("YOU SURE AREN'T GOING TO LIVE VERY LONG IF YOU CAN'T EVEN\nFOLLOW DIRECTIONS")
        moves()


def instruct():
    # 200
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
    A = input('Do you still want to continue?').upper()[0]
    if A is "N":
        fin(2)
    else:
        return


def advance(X):
    # 620
    S = input("How many Paces do you advance?")
    S = int(S)
    if -1 < S < 11:
        X = X - S
        print(f"You are now {X} paces apart.")
        return X
    elif S < 0:
        print("NONE OF THIS NEGATIVE STUFF PARTNER, ONLY POSITIVE NUMBERS")
    else:
        print("Nobody can walk that fast.")
    return advance(X)


def fire(C, X):
    # 690
    if C <= 3:
        C = C + 1
        W = randint(0, 10)  # original W=RND(-1)*10
        if W > X / 10:
            fin(1)
    # resp=[None,1460,1820,1840,710]
    # resp[C]()
    if C == 1 and P > 4:
        altbart()
    else:
        hit(P, C)
    return C


def jump():
    # 1410
    global T
    if T > 3:
        print("HOW MANY WATERING TROUGHS DO YOU THINK ARE ON THIS STREET")
        moves()
    else:
        print("NOT A BAD MANEUVER, YOU THREW BART'S STRATEGY OFF")


def give_up():
    # 1510
    print(
        "BLACK BART ACCEPTS. THE CONDITIONS ARE THAT HE WON'T SHOOT YOU\nIF YOU TAKE THE FIRST STAGE OUT OF TOWN AND "
        "NEVER COME BACK\nAGREED")
    H = input("Agreed?").upper()
    if H in {'N', 'NO'}:
        print("Oh well, Back to the showdown.")
        moves()
    else:
        fin(3)


def run(P):
    try:
        F = int(input("How far did you run?"))
    except:
        print("That's not a distance")
        moves()
        return
    if F >= 50:
        fin(4)
    elif P >= 4:
        fin(5)
    else:
        print(f"Black Bart Fires {4 - P} shells", '.' * 7)
        if P < 3:
            fin(6)
        else:
            fin(7)


def bart_move():
    # 1040
    global X, P
    Q = randint(0, 10)
    if X < 10 or Q > 5:
        P += 1
        if C <= 4:
            if P <= 4:
                bart_fire()
            elif P > 6:
                fin(8)
            else:
                if P == 5:
                    print("Now is your chance, Bart is out of shells")
                bart_pace()
        else:
            bart_pace()
    else:
        bart_pace()
    return


def bart_pace():
    # 1070
    global X
    Z = 2 + randint(0, 9)
    X = X - Z
    print(f"Black Bart moves {Z} paces.\nYou are now {X} paces apart")
    return


def bart_fire():
    # 1200
    global P, C, j
    R = randint(0, 10)
    print("Bart fires", "." * 6)
    if R > X / 10:
        if j:
            print("THAT TRICK SAVED YOUR LIFE. BART'S BULLET\nWAS STOPPED BY THE WOOD SIDES OF THE TROUGH.")
        else:
            fin(0)
    else:
        print("A miss", "." * 4)
        """if P>4: #impossible
                bart_pace()"""
        # resp=[None,1280,1890,1940,1960]
        miss(P, C)


def altbart():
    Q = randint(0, 10)
    if Q > 5:
        fin(8)
    else:
        bart_pace()
        moves()


def status(P, C):
    return "You now have " + str(4 - C) + " shells to Bart's " + str(4 - P) + " shells."


def miss(P, C):
    resp = [None]
    resp.append("Whew, were you lucky. That bullet just missed your head.\n" + status(1, C))
    resp.append("But Bart got you in the right shin.")
    resp.append("Though Bart got you on the left side of your jaw")
    resp.append("Bart Must have jerked the trigger")
    print(resp[P])


def hit(P, C):
    resp = [None]
    resp.append(status(P, 1))
    resp.append("Grazed Bart in the right arm")
    resp.append("HE'S HIT IN THE LEFT SHOULDER, FORCING HIM TO USE HIS RIGHT\nHAND TO SHOOT WITH")
    resp.append(
        "Nice going, ace. You've run out of shells.\nNow Bart won't shoot until you touch noses.\nYou better think of "
        "something fast (Like run).")
    print(resp[C])


def fin(x):
    # 2080
    global P
    resp = []
    resp.append("BART SHOT YOU RIGHT THROUGH THE HEART THAT TIME.\nYOU WENT KICKIN' WITH YOUR BOOTS ON.")  # resp[0]
    resp.append(
        "WHAT A SHOT, YOU GOT BART RIGHT BETWEEN THE EYES.\n\nAS MAYOR OF DODGE CITY, AND ON BEHALF OF ITS CITIZENS,"
        "\nI EXTEND TO YOU OUR THANKS, AND PRESENT YOU WITH THIS\nREWARD, A CHECK FOR $20,000, FOR KILLING BLACK "
        "BART.\n\n************************************************************\n\nCHECK NO."
        + str(randint(0, 100)) + "\t\t\t\tAUG."
        + str(randint(0, 10) + 10)
        + "TH. 1889\n\t\t   CASHIER'S "
          "RECEIT---BANK OF "
          "DODGE CITY\n\t\t\tPAY TO THE BEARER ON "
          "DEMAND\n\t\t\t\tTHE SUM OF\n\tTWENTY "
          "THOUSAND DOLLARS----------------------$20, 000\n\n"
          "************************************************************\n\n"
          "DON'T SPEND IT ALL IN ONE PLACE.")  # resp[1]
    resp.append("Greenhorn")  # 1370    resp[2]
    resp.append("A very wise decison.")  # resp[3]
    resp.append("MAN DID HE RUN. HE RAN SO FAST EVEN THE DOGS COULDN'T\nCATCH HIM")  # resp[4]
    resp.append(
        "YOU WERE LUCKY, BART CAN ONLY THROW HIS GUN AT YOU, HE\nDOESN'T HAVE ANY SHELLS LEFT. YOU SHOULD REALLY BE "
        "DEAD.")  # resp[5]
    resp.append("HE GOT YOU RIGHT IN THE BACK. THATS WHAT YOU DESERVE\n FOR RUNNING.")  # resp[6]
    resp.append(
        f"BLACK BART UNLOADED HIS GUN, ONCE IN YOUR BACK\nAND {3-P} TIMES IN YOUR A**. NOW YOU CAN'T EVEN REST IN "
        "\nPEACE.")  # resp[7]
    resp.append(
        "BART JUST HI-TAILED IT OUT OF TOWN RATHER THAN FACE YOU WITH-\nOUT A LOADED GUN. YOU CAN REST ASSURED THAT "
        "BART WON'T EVER\nSHOW HIS FACE AROUND THIS TOWN AGAIN.")  # resp[8]
    print(resp[x])
    print('\nC.G. INC')
    B = input('Do you want to play again?').upper()[0]  # Original: always stops the program
    if B is 'Y':
        main()
    else:
        exit()


main()

# Original (slightly edited by me) variables discriptions
#   D$--instruction need
#   A$--Intent to continue the game after receiving instructions -- not used
#   A---Stores your lucky number
#   I---Used for the random number generetor
#   X---Denotes the distance between you two
#   B---Denotes the number of your move choice
#   S---The number of paces you advance
#   C---Counter for the number of your shells
#   W---Random number for the hitting of bart
#   Q---Random number for Bart choice wheter to walk or fire
#   Z---Random number for the amount of paces bart advance
#   P---Counter for bart's remaining shells
#   R---random number for Bart's success at hitting you
#   T---counter for the number of watering troughs
#   F---Distance you have ran
#   H$--Decision on giving up
# variables that I came to add
#   j---binary value for wheter you've jump behind the watering trough
