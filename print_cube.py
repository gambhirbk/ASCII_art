CONST_NUMBER_TWO = 2
def main():
    '''
    function checks for valid input
    calls three other functions to make a cube
    '''
    cube_size = int(input("Input cube size (multiple of 2): "))
    if (cube_size % CONST_NUMBER_TWO != 0):
       cube_size = int(input("Not a multiple of 2. Try another cube size (multiple of 2): "))
    top_part_of_cube(cube_size)
    middle_part_of_cube(cube_size)
    tail_part_of_cube(cube_size)

def top_part_of_cube(n):
    ''' 
    top_part_of_cube functions take input number and 
    returns the top part of the cube
    n: user input multiple of 2 to make cube
    '''
    two_times_number = CONST_NUMBER_TWO * n
    floor_division_n = n//CONST_NUMBER_TWO
    space = n//CONST_NUMBER_TWO + 1
    print(" " * space + '+' + '-'* two_times_number + '+')

    k = space - 1 # k keeps track of the space in the front
    x = 0 # x keeps track of the space before '|' in the behind
    for _ in range (0,floor_division_n):
        print(" "* k + '/' + " "* two_times_number +'/'+ " "* x +'|')
        k-=1
        x+=1
    print('+' + '-' * two_times_number + '+' + " " * floor_division_n + '|')

def middle_part_of_cube(n):
    '''
    middle_part_of_cube takes the input number and builds the 
    middle part of the cube
    n: user input multiple of 2 to make cube
    '''
    two_times_number = CONST_NUMBER_TWO * n
    floor_division_n = n//CONST_NUMBER_TWO
    for i in range(n-floor_division_n, 0, -1):
        if i > 1:
            print("|" + " "* two_times_number + '|' + " "* floor_division_n + '|') 
        if i == 1:
            print("|" + " "* two_times_number + '|' + " "* floor_division_n + '+') 

def tail_part_of_cube(n):
    '''
    tail_part_of_cube take the input number and builds the 
    tail part of the cube
    n: user input multiple of 2 to make cube
    '''
    floor_division_n = n//CONST_NUMBER_TWO
    two_times_number = CONST_NUMBER_TWO * n
    space = n // CONST_NUMBER_TWO - 1 # to keep track of spaces 
    for _ in range(0, floor_division_n):
        print("|" + " "*two_times_number + "|" + " "* space + '/')
        space-=1
    print("+" + "-"* two_times_number + '+')

main()