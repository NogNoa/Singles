def insert():
    insert = True
    while insert:
        line = input()
        if line == ".":
            insert = False
        else:
            stream.append(line + "\n")


def expose(args):
    try:
        pl = int(args[0])
    except IndexError:
        for pl, line in enumerate(stream):
            print(f"{pl}\t{line}")
    except ValueError:
        if args[0] == ".":
            print(f"{focus}\t{stream[focus]}")
        else:
            print('?')
    else:
        print(f"{pl}\t{stream[pl]}")


def chose(args):
    try:
        line = int(args[0])
    except IndexError:
        print('?')
        return focus
    except ValueError:
        print('?')
        return focus
    else:
        return line


def delete(args):
    global stream
    try:
        line = int(args[0])
    except IndexError:
        print('???')
        if input() == "y":
            stream.clear()
            # That's just evil.
    except ValueError:
        if args[0] == ".":
            del stream[focus]
        else:
            print('?')
    else:
        del stream[line]


run = True
try:
    with open("the standard.txt", "r+") as file:
        stream = file.readlines()
except FileNotFoundError:
    stream = []
focus = 0

while run:
    line = input()
    if line == 'q':
        with open("the standard.txt", "w+") as file:
            file.write("".join(stream))
        run = False
    elif line == 'i':
        insert()
    elif line[0] == 'p':
        line = line.split(' ')
        expose(line[1:])
    elif line[0] == 'c':
        line = line.split(' ')
        focus = chose(line[1:])
    elif line[0] == 'd':
        line = line.split(' ')
        delete(line[1:])
    else:
        print("?")
