from numpy import *
from kNN import *


def make_data():
    #group is matrix of size 6 rows X 2 columns
    group = array([[3,104],[2,100],[1,81],[101,10],[99,5],[98,2]])
    labels = ['r','r','r','a','a','a']
    categories = {'r':'romance','a':'adventure'}
    return group, labels, categories
    
    
def main():
    #num kicks 1st parameter
    #num kisses 2nd parameter
    unknown = (90,18)  #90 kicks anbd 18 kisses. what kind of movie
    title = "Blade Runner"
    k = 3 #knn parameter
    
    group, labels, categories= make_data()
    type = classify(unknown,group,labels,k)
    print (title + ':' + categories[type])
    
main()
