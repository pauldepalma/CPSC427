'''
Demonstrates
   Pickle is python's object serializer.  Pickle functions can write python objects to
   files and read pickle files into python objects.

   Usage:
   >>from ex15 import pickle
   >>pickler()
   >>depickler()
'''

import pickle


def pickler():
    lsts_out = [ [i for i in range(10)] for j in range(5)]

    print "original matrix"
    for lst in lsts_out:
        print lst
    
    fout = open ('pickles.pkl','wb')
    pickle.dump(lsts_out,fout)

    fout.close()

    

def depickler():
    
    fin = open('pickles.pkl', 'rb')
    lsts_in = pickle.load(fin)

    print "pickled list"
    for lst in lsts_in:
        print lst

    fin.close()
    
