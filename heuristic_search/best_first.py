'''
program that creates a dict. representation of a tree from a data file
See make_tree for format
'''
from make_tree import *

#best-first traversal.  Depth-first but with the modificaiton that nodes
#are explored in order of value at each level.  The classic
# heuristic is f(n) = g(n) + h(n) where g is the path length
#and h is the heuristic value.  In this implementation, path length is
#ignored, effectively g(n) = 0
def best_first(tree, value, start):
    visited = [] #traversal list to eliminate cycles
    traverse = [] #traversal list with nodes and values
    stack = [start] #stack operations allow for depth-first search
    while stack: #returns true if list has items, false otherwise

        node = stack.pop()
        if node not in visited: #have we been here before
            visited.append(node)
            traverse.append(str(node) + ':' + str(value[node]))
            
        if tree[node] is not None: #is not a leaf node
            children = tree[node]
            #at each level sort the nodes by value so that they are explored
            #in best-first order
            children = sortNodes(children, value)
            children.reverse() #to simulate a stack
            for child in children:
                if child not in visited:
                    stack.append(child)
    return traverse

#Sort nodes by value.
def sortNodes(children,value):
    #Creates a list of tuples of the form (value, node) so that the
    #nodes can be sorted by value
    child_lst = [(value[child], child) for child in children]
    #getKey is invoked once for each tuple, implicitly accepting each tuple
    #in child_lst as an argument. In this case, we are sorting on the
    #0th element, i.e., the value
    child_lst = sorted(child_lst, key=getKey)
    #retrun the nodes, but now ordered by value
    children = [child[1] for child in child_lst]
    return children

def getKey(item):
    return item[0]
    
def main():
    tree_dict, value_dict = make_tree("tree.inp")
    print best_first(tree_dict, value_dict,'A')

    
    
             
main()
