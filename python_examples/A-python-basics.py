'''
Demonstrates
    program format
    nested if
    logical and
'''

def main():
    x = int(input("input an integer value for x\n"))
    y = int(input("input an integer value for y\n"))
    z = int(input("input an integer value for z\n"))
    
    if (x > y):
        if (x > z):
            print ("x is larger than both y and z")
        else:
            print ("x is not largest because it's not > z")              
    else:
        print ("x is not largest because it's not greater than y")

    if (x > y and x > z):
        big = x
    if (y > x and y > z):
        big = y
    if (z > x and z > y):
        big = z

    print(str(big) + " is largest")  

main()

   


