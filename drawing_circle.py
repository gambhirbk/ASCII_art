import math
import sys

# draw_circle returns a circle
# radius: radius of the circle


def draw_circle(radius):
    SQUARED = 2
    for width in range(radius * SQUARED):
        for height in range(radius * SQUARED):
            dist = math.sqrt(((abs(width-radius)) ** SQUARED) +
                             ((abs(height-radius)) ** SQUARED))
            if (dist < radius):
                print("0", end='')
            else:
                print(" ", end='')

        print()


draw_circle(int(sys.argv[1]))
