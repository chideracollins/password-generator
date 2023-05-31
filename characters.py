import random


def character(ch_type):
    _alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    _alpha_upper = [x.upper() for x in _alpha]
    _alpha.extend(_alpha_upper)
    _numeric = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    _symbol = ('~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '=', '-', '<', '<', '/', '?')
    return random.choice(locals()[ch_type])


