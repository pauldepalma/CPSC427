'''
Based on AB prune pseudo-code found in:
Nilsson, N. (2009). AI: A New Synthesis. San Francisco:Morgan-kaufman.
'''

import pickle

visited = []  #stores nodes visited during traversal
tree = {}     #stores tree.  See make_tree.py for format

#distinguishes between a character node name and an integer leaf node value
def is_value(n):
    try:
        int(n)
    except ValueError:
        return False
    return True

'''
It's possible to collapse this and the following function
But the object is clarity
The levels are interpreted differently, depending upon whether MAX or MIN is root
'''
def AB_MAX(n,alpha,beta):
    stuff = tree[n]     #information about node n.  See make_tree.py
    level = stuff[0]    #extract level
    children = stuff[1] #extract list of chldren or value
    potential_value = children[0] #either a node name or a value if a leaf node
    if is_value(potential_value):
        return potential_value
    
    b = len(children) #variable b is used to be consistent with pseudo-code

    for k in range (b): #variable k is used to be consistent with pseudo-code
        n = children[k]  
        visited.append(n)
        if (level % 2 == 0):
            alpha = max(alpha,AB_MAX(n,alpha,beta))
            if alpha >= beta:
                return beta
        if (level % 2 > 0):
            beta = min(beta,AB_MAX(n,alpha,beta))
            if beta <= alpha:
                return alpha    
    if (level % 2 == 0):
        return alpha
    else:
        return beta

def AB_MIN(n,alpha,beta):
    stuff = tree[n]    #info from entry for node n
    level = stuff[0]   #extract level of node n
    children = stuff[1]#extract list of chldren or, if leaf, extract value
    potential_value = children[0] #1st child or, if leaf, value
    if is_value(potential_value):
        return potential_value
    
    b = len(children)
    for k in range (b):
        n = children[k]
        visited.append(n)
        if (level % 2 == 0):
            beta = min(beta,AB_MIN(n,alpha,beta))
            if beta <= alpha:
                return alpha
        if (level % 2 > 0):       
            alpha = max(alpha,AB_MIN(n,alpha,beta))
            if alpha >= beta:
                return beta
    if (level % 2 == 0):
        return beta
    else:
        return alpha
    
def main():
    global visited
    global tree

    tree = pickle.load(open("tree.p","rb"))
    start = open("start.p","r")
    root = start.read()
    alpha = -1000
    beta = 1000

    visited.append('r')

    if root == "MAX":
        print AB_MAX("r",alpha,beta)
    else:
        print AB_MIN("r",alpha,beta)
    print visited
    
             
main()
