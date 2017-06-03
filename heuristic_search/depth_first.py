'''
program that creates a dict. representation of a tree from a data file
See make_tree for format
'''
from make_tree import *

#iterative version of depth_first, pre-order traversal
def depth_first(tree, value, start):
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
            children.reverse() #so we can traverse left to right
            for child in children:
                if child not in visited:
                    stack.append(child)
    return traverse

        

def main():
    tree_dict, value_dict = make_tree("tree.inp")
    print depth_first(tree_dict, value_dict,'A')

    
    
             
main()
