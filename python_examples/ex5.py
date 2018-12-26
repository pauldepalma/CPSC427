'''
Demonstrates:
    list structure
    tuple structure
    funcitons returning > 1 variable
    an approach to error checking
'''

import random

LOW = 1
HIGH = 100

def make_list(size):
    lst = []
    for i in range(size):
        lst.append(random.randint(LOW,HIGH))
    return lst


def get_size():
    while(True):
        size = int(input("How many items should I put in the list?  "))
        if size < 1:
            print("Number of items must exceed 0.  Try again.")
        else:
            return size

#Note the use of "in" with a tuple
def get_direction():
    while(True):
        direction = raw_input("Print top to bottom or bottom to top (T/B)?  ")
       
        if direction not in ('T','B'):
            print("Direction must be T or B.  Try again.")
        else:
            return direction

def set_choices(lst,direction):
    if direction == 'T':
        start = 0
        stop = len(lst)
        inc = 1
    else:
        start = len(lst) - 1
        stop = -1
        inc = -1

    return start, stop, inc
    

def disp_list(lst,direction,start,stop,inc):
    

    print "using a while loop"
    if direction == 'T':
        while start < stop:
            print (lst[start])
            start += 1

    if direction == 'B':
        while start > stop:
            print (lst[start])
            start -= 1
            
    print "Here's how the opposite choice would look"
    if direction == 'T':
        direction = 'B'
    else:
        direction = 'T'

    start, stop, inc = set_choices(lst,direction)

    print "using a for loop"
    if direction == 'T':
        for i in range(start,stop,inc):
            print (lst[i])


    if direction == 'B':
        for i in range(start,stop,inc):
            print (lst[i])
def main():

    size = get_size()
    direction = get_direction()
    lst = make_list(size)
    start, stop, inc = set_choices(lst,direction) #return > 1 variable
    disp_list(lst,direction,start,stop,inc)

main()
    
