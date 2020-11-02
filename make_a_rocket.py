import sys 

CONST_NUM_TWO = 2
CONST_NUM_FOUR = 4
# main function returns the rocket without stripped 
# if the argument is None; otherwise returns a rocket with stripped 
# optional_argument: optional arguments to track if users input stripped or not
def main(optional_argument = None):
    width = int(sys.argv[1])
    square = int(sys.argv[CONST_NUM_TWO])
    nose_cone(width)
    if len(sys.argv) >= CONST_NUM_FOUR:
        fuselage_striped(width, square)
    else:
        fuselage_without_striped(width, square)
    tail(width, square)
   
# nose_cone returns the top part of the rocket
def nose_cone(width):
    row_space = width//CONST_NUM_TWO
    row_asterik = width % CONST_NUM_TWO
    for i in range(row_asterik, width, CONST_NUM_TWO):
        print(' '*row_space + i * '*')
        row_space = row_space-1  

# fuselage_without_stripped returns the middle part of the rocket without stripped
def fuselage_without_striped(width, square):
    for _ in range(1, square+1):
        for _ in range(width):
            print ('x'* width)
            
# fuselage_stripped returns the middle part of the rocket with stripped
def fuselage_striped(width, square):
    if width % square == 0:
        strip_num = width // square 
    else:
        strip_num = width // square + CONST_NUM_TWO
    for i in range(1, square+1):
        for i in range(1,width+1):
            if i <= strip_num:
                print('-' * width)
            else:
                print('X' * width)

# tail returns the tail of the rocket 
def tail(width, square):
    square_1 = square+1
    row_space_2 = width//CONST_NUM_TWO 
    for i in range(row_space_2, width+1, CONST_NUM_TWO):
        print(' '*square_1 + i * '*')
        square_1 = square_1-1
    print('*'* width)

main()
