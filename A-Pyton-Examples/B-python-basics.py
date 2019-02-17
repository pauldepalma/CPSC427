'''
Demonstrates:
    program format
    constants
    function without return value
    input
    random library
    for loop
    strings
'''


import random

#global constants.  scope is the entire program
HEADS = 0
TAILS = 1

def gen_tosses(tosses):
    for toss in range(tosses):
        out_str = 'Toss ' + str(toss + 1) + '\t'    #notice the tab character
        if random.randint(HEADS,TAILS) == HEADS:
            print(out_str + 'heads')
        else:
            print(out_str + 'tails')

def main():
    tosses = int(input('Enter the number of tosses '))
    gen_tosses(tosses)
    
main()
    
 
