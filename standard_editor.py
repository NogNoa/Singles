import argparse

help_str = """
A line editor inspired by Unix ed

In the main command mode, enter an input of the form <action argument>
All actions are single letter. arguments are either an integer, nothing or either of '.' '*' without the apostrophes

Arguments:
Integer - Targets a specific line. Line indeces start at 0.
. -       Targets the line that is in focus.
* -       Targets all lines. 
empty   - Giving no additional argument always act as '.'

Actions:
c - Changes the line that is in focus. 
    . print the current focus.
    * targets the end of the file.

d - Deletes line.

e - Enters an edit mode that let you replace a segment of text with another.
    The syntax is old/new/old/new... Deleting a segment with a final / is possible.

i - Enters an input mode that let you insert text into the file.
    * targets the end of the file. 
    To exit the input mode enter a line consisting only of '.'
    When you do, focus will automatically pass to the end of the inserted text.

m- Moves by copy the line in focus to the target.
    md - deletes the original as well
    * targets the end of the file

p - prints line to the console.

q - Saves the file and exit the program.
    unique argument '!' to not save.

Back to Python's Help message:
"""


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
    global focus
    if mode == '?':
        print("?")
        return
    r_insert = True
    cache = []
    while r_insert:
        line = input()
        if line == ".":
            r_insert = False
            if mode == '*':
                stream.extend(cache)
                focus = len(stream) - 1
            elif mode == '.':
                stream[focus:focus] = cache
                focus += len(cache)
            else:
                stream[mode:mode] = cache
                focus = mode + len(cache)
            print(focus)
        else:
            cache.append(line + '\n')


def edit(mode):
    if mode == '?':
        print("?")
        return
    elif mode == '.':
        mode = focus

    def tr(cmd, line):
        global stream
        for pl, string in enumerate(cmd[::2]):
            stream[line].replace(string, cmd[pl + 1])

    cmd = input()
    cmd = cmd.split('/')
    if len(cmd) % 2:
        _ = cmd.pop()

    if mode == '*':
        for line, _ in enumerate(stream):
            tr(cmd, line)
    else:
        tr(cmd, mode)
        print(stream[mode])


def expose(arg):
    arg = parse(arg)
    if arg == '*':
        for pl, line in enumerate(stream):
            print(f"{pl}  {line}")
    elif arg == '.':
        print(f"{focus}  {stream[focus]}")
    elif arg == '?':
        print('?')
    else:
        print(f"{arg}  {stream[arg]}")


def chose(arg):
    arg = parse(arg)
    if arg == '?':
        print('?')
        return focus
    elif arg == '.':
        print(focus)
        return focus
    elif arg == '*':
        return len(stream) - 1
    else:
        return arg


def delete(arg):
    global stream
    arg = parse(arg)
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


def move(arg, focus):
    arg = parse(arg)
    cache = stream[focus]
    if arg == '*':
        stream.append(cache)
    elif arg == '.':
        stream.insert(focus, cache)
    else:
        stream.insert(arg + 1, cache)


parser = argparse.ArgumentParser(description=help_str, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('name', default="the standard.txt", help="Name of the file you want to edit")
name = parser.parse_args().name
run = True

try:
    with open(name, "r+") as file:
        stream = file.readlines()
except FileNotFoundError:
    stream = []
focus = len(stream) - 1
print(focus)

while run:
    line = input().split(' ')
    if line[0] == 'q':
        if not line[1:] == ['!']:
            with open(name, "w+") as file:
                file.write("".join(stream))
        run = False
    elif line[0] == 'i':
        mode = parse(line[1:])
        insert(mode)
    elif line[0] == 'p':
        expose(line[1:])
    elif line[0] == 'c':
        focus = chose(line[1:])
    elif line[0] == 'd':
        delete(line[1:])
    elif line[0] == 'e':
        mode = parse(line[1:])
        edit(mode)
    elif line[0][0] == 'm':
        move(line[1:], focus)
        if line[0] == 'md':
            delete([focus])

    else:
        print("?")

# TODO edit() keep the line unchanged
