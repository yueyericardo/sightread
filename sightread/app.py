#!/usr/bin/env python
import numpy as np
import os
from playsound import playsound


def info(text):
    print('\033[32m{}\33[0m'.format(text))  # green


def parseinput():
    ipt = input()
    opt = []
    for i in ipt:
        if i.isdigit():
            ii = int(i)
            if ii < 8 and ii > 0:
                opt.append(ii)
            else:
                print(f'warning: {ii}')
    opt = np.array(opt) - 1
    return opt


num = np.array(['1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  '])
note = np.array(['do ', 're ', 'mi ', 'fa ', 'sol', 'la ', 'si '])
c = np.array(['C', 'D', 'E', 'F', 'G', 'A', 'B'])
path = os.path.dirname(os.path.realpath(__file__))


def singnotes(randnotes, verbose=False):
    if verbose:
        print(f"{' '.join(num[randnotes])}")
        info(f"{' '.join(note[randnotes])}")
    for i in randnotes:
        mp3file = os.path.join(path, f'mp3/{i+1}.m4a')
        playsound(mp3file)


if __name__ == "__main__":  
    # 676311771
    # 556517
    info('Keep Practicing!\n')
    mode = input("Select Mode: \n1: Single \n2: Mix \n3: Long \n4: Custom\n5: Input Note\n\n")
    if mode == '':
        mode = 2
    else:
        mode = int(mode)
    assert mode >= 1 and mode <= 5
    print()
    if mode == 4:
        size = int(input("Input Length: "))
    info("\nStart\n")

    while(True):
        iptnotes = None
        if mode == 1:
            size = np.random.choice(np.arange(1, 2), 1)[0]
        elif mode == 2:
            size = np.random.choice(np.arange(1, 6), 1)[0]
        elif mode == 3:
            size = np.random.choice(np.arange(3, 5), 1)[0]
        elif mode == 5:
            size = np.random.choice(np.arange(3, 5), 1)[0]
            iptnotes = parseinput()
        if iptnotes is None:
            randnotes = np.random.randint(0, 7, size)
            info(f"{' '.join(note[randnotes])}".format(input(f"{' '.join(num[randnotes])}")))
            singnotes(randnotes, verbose=False)
        else:
            randnotes = iptnotes
            singnotes(randnotes, verbose=True)
