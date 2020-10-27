# this program prints the diamond of stars

import sys

# diamond function returns the diamond shaped of
# input height


def diamond(height):
    CONST_NUM_TWO = 2
    # for loop to print the top half of the diamond
    # +1 since the loop begins with 0 and need top row
    # center command to center the top half of the diamond

    for h in range(height):
        if h % CONST_NUM_TWO == 0:
            s = '*' * (h+1)
            print(s.center(height, ' '))

    # for loop to print the bottom half of the diamond
    # reversed to have diamond print downwards
    for h in reversed(range(height)):
        if h % CONST_NUM_TWO != 0:
            s = '*' * h
            print(s.center(height, ' '))


diamond(int(sys.argv[1]))
