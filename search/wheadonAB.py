
'''
The Wheadon AB Prune


*********************************************************************
Best First Search with MiniMax and Alpha-Beta Pruning
*********************************************************************

TO RUN:
Just run this file in a python IDE. It calls the main function and will print out the
nodes visited in order, leaving out the nodes pruned.

The tree searched is the same the hand trace of AB prune, item 9 on the class web page.  

'''



def maxVal(graph,node,alpha,beta):
    print node
    if isinstance(node,int):
        return node
    v = float("-inf")
    for child in graph.get(node):
        v1 = minVal(graph,child,alpha,beta)
        if v == 'null' or v1 > v:
            v = v1
        if beta != 'null':
            if v1 >= beta:
                return v
        if alpha == 'null' or v1 > alpha:
            alpha = v1
    return v

def minVal(graph,node,alpha,beta):
    print node
    if isinstance(node,int):
        return node
    v = float("inf")
    for child in graph.get(node):
        v1 = maxVal(graph,child,alpha,beta)
        if v == 'null' or v1 < v:
            v = v1
        if alpha != 'null':
            if v1 <= alpha:
                return v
        if beta == 'null' or v1 < beta:
            beta = v1
    return v


def main():
    '''
    graph = {'A' : ['P', 'B'],
             'B' : [5,100],
             'C' : ['A', 'D', 'E'],
             'D' : ['R', 42],
             'E' : ['T', 'V'],
             'P' : [2,3],
             'R' : [0],
             'T' : [2,1],
             'V' : [9,11]
             }
    
    maxVal(graph,'C','null','null')
    '''
    graph = {'A' : ['B', 'C'],
             'B' : ['D','E'],
             'C' : [0, 'G'],
             'D' : [1, 5, 8],
             'E' : [9,3],
             'G' : [1,100]
             }
    
    maxVal(graph,'A','null','null')  #root is max


if __name__ == '__main__':
    main()
