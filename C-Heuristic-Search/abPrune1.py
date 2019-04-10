
'''
Class: CPSC 427 
Team Member 1: Paul De Palma
Team Member 2: None
Submitted By Paul De Palma
GU Username: depalma
File Name: abPrune1.py
Demonstrates AB Pruning:
--reads file representation of a tree as input
--converts the file to a dictionary representation of a tree
--implements the pseudo-code found on slide 28, E:Adversarial Games
--the pseudo-code is from a classic book on AI: 
  (Nilsson, N. (1998). Artificial Intelligence: A New Synthesis. 
  Morgan Kaufmann)
--Jeff Wheadon (GU, class of 2018) wrote the 1st draft of maxVal and minVal
--Differs from abPrune1.py in that nodes are represented as tuples: (M,8)
  Requires input in a different format (see abEx1-1.txt vs. abEx1.txt
Usage 1:  python <program name> <file name> <player>
          python proj9_abPrune.py abEx1-1.txt max

Usage 2: The program can also be run from idle, in which case the 
         parameters must be hard-coded
'''

import sys

def maxVal(graph,node,alpha,beta):
    print node[0]
    if node[1] > 0:
        return node[1]
    v = float("-inf")
    for child in graph.get(node):
        v1 = minVal(graph,child,alpha,beta)
        if v is None or v1 > v:
            v = v1
        if beta is not None:
            if v1 >= beta:
                return v
        if alpha is None or v1 > alpha:
            alpha = v1
    return v

def minVal(graph,node,alpha,beta):
    print node[0]
    if node[1] > 0:
        return node[1]
    v = float("inf")
    for child in graph.get(node):
        v1 = maxVal(graph,child,alpha,beta)
        if v is None or v1 < v:
            v = v1
        if alpha is not None:
            if v1 <= alpha:
                return v
        if beta is None or v1 < beta:
            beta = v1
    return v
'''
Transforms an input file to a dictionary representation of a graph
This is abEx1.txt
Input File
S,0 G,0
G,0 J,0 K,0
J,0 M,8, Z,12
K,0 N,4 T,0
P,100 Q,2, R,3

Where:
Each row a parent node followed by its children.
The numbers are the values of the nodes.  All internal nodes have value 0
The first line indicates that G is the start node in the graph traversal
The resulting dictionary will looks like this:
{
  ('G',0): [('J',0), ('K',0)]
  ('J',0): [('M',8), ('Z',12)]
  ('K',0): [('N',4), ('T',0)]
  ('T',0): [('P',100), ('Q',2), ('R',3)]
}
'''
def read_graph(file_name):
    #construct a dictionary from the input file
    with open(file_name) as fin:
        rows = (line.rstrip() for line in fin)
        rows = [r.split() for r in rows]

    tuples = [ [tuple(node.split(',')) for node in row] for row in rows]
    graph = {row[0]:[row[i] for i in range(1,len(row))] for row in tuples}
    root = graph[('S', '0')][0]
    del graph[('S', '0')]

    #transform digits in leaf nodes from strings to numeric values
    for key in graph.keys():
       graph[key] = [  (elt[0], int(elt[1])) for elt in graph[key]  ]

    #transform digits in keys from strings to numeric values
    for key in graph.keys():
        newKey = (key[0],int(key[1]))
        graph[newKey] = graph.pop(key)

    #transform digit in root from string to numerric value
    root = (root[0],0)
    
    return root,graph

def AB(graph,root,alpha,beta,player):
    if player == 'max':
        maxVal(graph,root,alpha, beta)
    else:
        minVal(graph,root,alpha,beta)
        

def main():
    if len(sys.argv) > 1:           #parameters come from command line  
        file_name = sys.argv[1]  
        player = sys.argv[2]
    else:
        file_name = 'abEx1-1.txt'     #default
        player = 'max'

    root, graph = read_graph(file_name)
    AB(graph,root, None, None, player)

main()
