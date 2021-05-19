#!/usr/bin/env python3

import argparse

help_str = """
A line editor inspired by Unix ed

In the main command mode, enter an input of the form <action argument>
All actions are single letter. arguments are either an integer, nothing or either of '.' '*' without the apostrophes

Arguments:
Integer - Targets a specific line. Line indeces starts at 0.
. -       Targets the line that is in focus.
* -       Targets all lines. 
empty   - Giving no additional argument always acts as '.'

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

j - Joins a line with the one after it
    * targets the line before the last.

m- Moves by copy the line in focus to the target.
    md - deletes the original as well
    * targets the end of the file

p - Prints line to the console.

q - Saves the file and exits the program.
    unique argument '!' to not save.
    
v - Divides a line.
    * targets the end of the file.
    Enters a divide mode where you need to enter a phrase.
    The line will be divided immedietly after every single occurance of the phrase.
    To exit divide mode, enter an empty line or '.'. to divide on a '.' just add charecters before it.

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
        if line >= len(stream):
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
        old = cmd[::2]
        new = cmd[1::2]
        for pl, old_str in enumerate(old):
            stream[line] = stream[line].replace(old_str, new[pl])

    cmd = input()
    cmd = cmd.split('/')
    if len(cmd) % 2:
        _ = cmd.pop()

    if mode == '*':
        for line, _ in enumerate(stream):
            tr(cmd, line)
    else:
        tr(cmd, mode)
        print(f"{mode}  {stream[mode]}")


def expose(mode):
    if mode == '*':
        for pl, line in enumerate(stream):
            print(f"{pl}  {line}")
    elif mode == '.':
        print(f"{focus}  {stream[focus]}")
    elif mode == '?':
        print('?')
    else:
        print(f"{mode}  {stream[mode]}")


def chose(mode):
    if mode == '?':
        print('?')
        return focus
    elif mode == '.':
        print(focus)
        return focus
    elif mode == '*':
        return len(stream) - 1
    else:
        return min(mode, len(stream) - 1)


def delete(mode):
    global stream, focus
    if mode == '*':
        print('???')
        if input() == "y":
            stream.clear()
            # That's just evil.
    elif mode == '.':
        del stream[focus]
    elif mode == '?':
        print('?')
    else:
        del stream[mode]

    if not stream:
        stream = ['']
    focus = min(len(stream) - 1, focus)


def move(mode):
    global stream
    cache = stream[focus]
    if mode == '?':
        print('?')
    elif mode == '*':
        stream.append(cache)
    elif mode == '.':
        stream.insert(focus, cache)
    else:
        stream.insert(mode, cache)


def divide(mode):
    global stream

    def div_main(pl_line, line):
        pl_phrs = line.find(phrs)
        while pl_phrs != -1:
            stream[pl_line] = line[:pl_phrs]
            stream.insert(pl_line + 1, line[pl_phrs:])
            line = line[pl_phrs+len(phrs):]
            pl_phrs = line.find(phrs)

    if mode == '?':
        print("?")
        return
    elif mode == '.':
        mode = focus
    phrs = input()
    if phrs in {'.', ''}:
        return
    if mode == '*':
        for pl_line, line in enumerate(stream):
            div_main(pl_line, line)
    else:
        div_main(mode, stream[mode])


def join(mode):
    global stream
    if mode == '?':
        print("?")
        return
    elif mode == '.':
        mode = focus
    if mode in {'*', len(stream) - 1}:
        mode = len(stream) - 2
    cache = stream[mode + 1]
    delete(mode + 1)
    stream[mode].append(' ' + cache)


parser = argparse.ArgumentParser(description=help_str, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument('-n', default="the standard.txt", help="Name of the file you want to edit")
name = parser.parse_args().n
run = True

try:
    with open(name, "r+") as file:
        stream = file.readlines()
except FileNotFoundError:
    stream = ['']
focus = len(stream) - 1
print(focus)

while run:
    line = input().split(' ')
    act = line[0]
    mode = parse(line[1:])
    try:
        if act == 'q':
            if not line[1:] == ['!']:
                with open(name, "w+") as file:
                    file.write("".join(stream))
            run = False
        elif act == 'i':
            insert(mode)
        elif act == 'p':
            expose(mode)
        elif act == 'c':
            focus = chose(mode)
        elif act == 'd':
            delete(mode)
        elif act == 'e':
            edit(mode)
        elif act == 'v':
            divide(mode)
        elif act == 'j':
            join(mode)
        elif act[:1] == 'm':
            move(mode)
            if line[0] == 'md':
                delete(focus)
            focus = chose(mode)
        else:
            print("?")
    except Exception as error:
        with open(name + '.bak', "w+") as file:
            file.write("".join(stream))
            print(f"Something bad happened. But a backup of your file was saved as {name}.bak")
        raise error

#  todo: make choose the only place where focus changes
#        move global focus inside choose() than.
#        join and divide: the stream is actually a list not \n separated text.
#        recursion not a while loop
#  done: get the parsing out of chose so edit
#       bug with md 2 (mode was list because we try to enter input for parse and than moved parse out)
#       move change focus with chose
#       by delete focus can still get over the end
