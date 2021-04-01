def parse(args):
    try:
        line = int(args[0])
    except IndexError:
        return '.'
    except ValueError:
        if args[0] in {'.', '*'}:
            return args[0]
        else:
            return '?'
    else:
        return line


def insert(mode):
    if mode == '?':
        print("?")
        return
    insert = True
    cache = []
    while insert:
        line = input()
        if line == ".":
            insert = False
            if mode == '*':
                stream.extend(cache)
            elif mode == '.':
                stream[focus:focus] = cache
            else:
                stream[mode:mode] = cache
        else:
            cache.append(line + '\n')


def expose(args):
    arg = parse(args)
    if arg == '*':
        for pl, line in enumerate(stream):
            print(f"{pl}\t{line}")
    elif arg == '.':
        print(f"{focus}\t{stream[focus]}")
    elif arg == '?':
        print('?')
    else:
        print(f"{arg}\t{stream[arg]}")


def chose(args):
    arg = parse(args)
    if arg in {'*', '.', '?'}:
        print('?')
        return focus
    else:
        return arg


def delete(args):
    global stream
    arg = parse(args)
    if arg == '*':
        print('???')
        if input() == "y":
            stream.clear()
            # That's just evil.
    elif arg == '.':
        del stream[focus]
    elif arg == '?':
        print('?')
    else:
        del stream[arg]


name = "the standard.txt"
run = True
try:
    with open(name, "r+") as file:
        stream = file.readlines()
except FileNotFoundError:
    stream = []
focus = 0

while run:
    line = input()
    if line == 'q':
        with open(name, "w+") as file:
            file.write("".join(stream))
        run = False
    elif line[0] == 'i':
        mode = parse(line[1:])
        insert(mode)
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
