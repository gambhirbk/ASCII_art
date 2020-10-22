
# Input from the user 'base' defines the base of the tree
# Divide the tree into three parts in height direction - when at height,
# at base and the remaining
# Divide the three into two parts width wise - left and right


def main():

    EVEN_DIVIDER = 2
    num = int(input("Please enter an odd number: "))

    while (num % EVEN_DIVIDER == 0):
        num = int(input("You chose a even number!  Please enter an odd \
number: "))

    UNDERSCORE = '_'
    SPACE = ' '
    STAR = '*'
    FRONT_SLASH = '/'
    BACK_SLASH = '\\'

    tree_base = num - EVEN_DIVIDER
    row = (num + 1) // EVEN_DIVIDER

    for i in range(row):
        len_middle = (i*2)+1
        side_space = (num-len_middle) // EVEN_DIVIDER
        if (i == 0):
            print(side_space * SPACE + STAR + side_space * SPACE)
        elif (i < row-1):
            print(side_space * SPACE + FRONT_SLASH +
                  (len_middle - EVEN_DIVIDER) * SPACE +
                  BACK_SLASH + SPACE * side_space)
        else:
            print(FRONT_SLASH + tree_base*UNDERSCORE + BACK_SLASH)


main()
