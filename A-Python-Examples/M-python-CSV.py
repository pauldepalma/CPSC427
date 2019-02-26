'''
Demonstrates:
   Reading a CSV file into a numpy array
   Usage: python M-python-CSV.py M-python-CSV.csv 
'''

import csv
import numpy
import sys

def main():
    
    fin = sys.argv[1]
    reader = list(csv.reader(open(fin, "rb"), delimiter= ','))

    result = numpy.array(reader).astype('float')
    print result
  
    #another way to read csv files into a numpy array

    result = numpy.genfromtxt(sys.argv[1],delimiter=',')
    print result
    
main()
