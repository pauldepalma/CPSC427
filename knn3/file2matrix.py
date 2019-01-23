import kNN
from numpy import *

def file2matrix(fnIn):
    fn = open(fnIn)
    numLines = len(fn.readlines())
    mat = zeros((numLines,3))
    print mat


def main():
    file2matrix("datIn.txt")

main()
