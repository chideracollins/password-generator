from characters import character
import random


def _ratio(lvl, length):
    ratio = list()
    ratio_1_2 = {1: [0.6, 0.3, 0.1], 2: [0.4, 0.4, 0.2]}
    position = 0
    while position < 3:
        if lvl == 3:
            ratio.append(round(0.3 * length))
        else:
            ratio.append(round(ratio_1_2[lvl][position] * length))
        position += 1
    if sum(ratio) < length:
        increment = length - sum(ratio)
        index = random.randint(0, 2)
        ratio[index] = ratio[index] + increment
    elif sum(ratio) > length:
        index = random.randint(0, 2)
        ratio[index] = ratio[index] - 1
    return ratio


def obtain_ch(ch_type, size, lvl):
    ch_list = list()
    while len(ch_list) < size:
        ch = character(ch_type)
        if lvl == 3 and ch not in ch_list:
            ch_list.append(ch)
        elif lvl == 2 and ch_list.count(ch) < 2:
            ch_list.append(ch)
        elif lvl == 1:
            ch_list.append(ch)
    return ch_list


def generate(level: int = '1', length: int = -1, ch_type_size=0) -> str:
    pass_ch = list()
    if ch_type_size == 0:
        if level == '1' or length == -1:
            if level == '1':
                level = random.randint(1, 3)
            length = random.randint(8, 15)
        ch_type_size = _ratio(level, length)
    n = 0
    for type_ in ("_alpha", "_numeric", "_symbol"):
        pass_ch.extend(obtain_ch(type_, ch_type_size[n], int(level)))
        n += 1
    random.shuffle(pass_ch)
    return ''.join(pass_ch)
