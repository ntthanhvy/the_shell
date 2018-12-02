#!/usr/bin/env python3

import os


def parse_input(str):
    if '$(' in str:

    words = str.split()
    print(words)
    commands = []
    operator = []
    special_char = ['||', '|', '&&', ';', '<', '>']
    cmd = []
    count = 0
    for word in words:
        # print('time:', count)
        if word not in special_char:
            # print(word)
            cmd.append(word)
        else:
            commands.append(cmd)
            operator.append(word)
            cmd = []
    commands.append(cmd)
    for command in commands:
        command = [command[0], ' '.join(command[1:])]
    return commands, operator


def main():
    check = True
    while check:
        print('intek-sh$ ', end='')
        stdin = input()
        commands, operator = parse_input(stdin)
        print(commands, operator)
        # for command in commands:



try:
    main()
except EOFError:
    pass
