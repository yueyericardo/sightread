#!/usr/bin/env python
import numpy as np
from playsound import playsound

a = np.array(['1  ', '2  ', '3  ', '4  ', '5  ', '6  ', '7  '])
b = np.array(['do ', 're ', 'mi ', 'fa ', 'sol', 'la ', 'si '])
c = np.array(['C', 'D', 'E', 'F', 'G', 'A', 'B'])


def info(text):
    print('\033[32m{}\33[0m'.format(text))  # green


info('Keep Practicing!\n')
t = 0
mode = input("Select Mode: \n1: Single \n2: Mix \n3: Long \n4: Custom\n")
mode = int(mode)
assert mode == 1 or mode == 2 or mode == 3 or mode == 4
print()
if mode == 1:
    size = np.random.choice(np.arange(1, 2), 1)[0]
if mode == 2:
    size = np.random.choice(np.arange(1, 6), 1, p=[0.5, 0.2, 0.1, 0.1, 0.1])[0]
if mode == 3:
    size = np.random.choice(np.arange(3, 5), 1)[0]
if mode == 4:
    size = int(input("Input Length: "))
info("\nStart\n")

while(True):
    randints = np.random.randint(0, 7, size)
    info(f"{' '.join(b[randints])}".format(input(f"{' '.join(a[randints])}")))
    for i in randints:
        playsound(f'mp3/{i+1}.m4a')
    t += 1
