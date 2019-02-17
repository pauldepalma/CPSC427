'''
Demonstrates:
   Reading a CSV file into a numpy array
   Usage: python 3x17.py matrix.csv
'''

import csv
import numpy
import sys

def main():
    fin = sys.argv[1]
    reader = csv.reader(open(fin, 'rb'), delimiter= ',')

    x = list(reader)

    result = numpy.array(x).astype('float')
    print fin
    '''
    print sys.argv[2]
    print sys.argv[3]
    stuff = sys.argv[3]
    print stuff[0]
    print stuff[1]
    print stuff[2]
    '''
    print result
   
    for item in result:
        print item
    
    
main()
