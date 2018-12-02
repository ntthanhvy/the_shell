#!/usr/bin/env python3


def do_indirection(str, vars):
    pass


# return the Error of the parameter
def do_error(str, vars):
    para_err = str.split('?')
    print(para_err)
    if para_err[0].strip(':') not in vars or vars[para_err[0].strip(':')] == '':
        error = 'parameter is null or not set'
        if para_err[1] is not '':
            error = para_err[1]
        return('intek-sh: ' + para_err[0].strip(':') + ': ' + error)
    else:
        return vars[para_err[0].strip(':')]


def result(str, variables):
    if '$' in str:
        para = str.strip('$').strip('{}')
        if para.startswith("#"):
            # This will get the len of the parameter '''
            if para.strip('#') in variables:
                return(len(para.strip('#')))
            else:
                return 0
        elif para.startswith('!'):
            # This will return the value of the value of the parameter
            if '*' in para or '@' in para:
                # variable expansion
                # do_var_expand(para)
                print('var expansion')
            else:
                # do_indirection(para)
                print('value of value of para')
        elif ':' in para and para.split(':')[1].isdigit():
            '''case 1: is slicing the parameter from the start to end, separate by
             colon (:)'''
            # do_substring(para)
            print('slicing')
        elif '#' in para or '%' in para:
            # substring removal
            # do_substr_remove(para)
            print('substring remove')
        elif '^' in para or ',' in para or '~' in para:
            # case modified
            # do_case_mod(para)
            print('case modified')
        elif '/' in para:
            # search and replace
            # do_search(para)
            # do_replace(para)
            print('search and replace')
        elif '-' in para:
            # use default value
            # do_default(para)
            print('use default')
        elif '=' in para:
            # assign a default value
            # do_assign(para)
            print('assign default')
        elif '+' in para:
            # use alternate value
            # do_altenate(para)
            print('use alternate')
        elif '?' in para:
            # display error if null or unset parameter
            return do_error(para, variables)
            print('display error')
        else:
            print('simple usage')
            if para in variables:
                return variables[para]
            else:
                return ''
    else:
        print('set var')
        return str
