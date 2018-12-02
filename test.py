#!/usr/bin/env python3

import parameter_expansion as para_ex


def store_var(vars, str):
    key, val = str.split('=')
    return {key: val}


def main():
    check = True
    vars = {}
    while check:
        print('intek-sh$ ', end='')
        stdin = input()
        if '=' in stdin:
            vars.update(store_var(vars, stdin))
        if '$' in stdin:
            # print(vars)
            print(para_ex.result(stdin, vars))


try:
    main()
except EOFError:
    pass
