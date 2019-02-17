'''
Demonstrates
  value returning function
'''

import random



def is_odd(num):
    if num % 2 == 0:
       return False
    else:
        return True

def main():
    for i in range(10):
        num = random.randint(0, 1000)
        if is_odd(num):
            print(str(num) + '\t' + 'odd')
        else:
            print(str(num) + '\t' +  'even')
    
main()
    
 
