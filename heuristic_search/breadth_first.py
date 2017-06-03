'''
make_tree is a python program that creates a dict rep. of a tree from a data
file.  See make_tree for format
'''
from make_tree import *

#iterative version of breadth_first traversal
def breadth_first(tree,value,start):
    visited = []
    traverse = []
    queue = [start]
    while queue: #returns true if list has items, false otherwise
        node = queue.pop(0) #dequeue
        if node not in visited: #have we been here before
            visited.append(node)
            traverse.append(str(node) + ':' + str(value[node]))

        if tree[node] is not None: #is not a leaf node
            children = tree[node]
            for child in children:
                if child not in visited:
                    queue.append(child)       
    return traverse
 

def main():
    tree_dict, value_dict = make_tree("tree.inp")
    print breadth_first(tree_dict,value_dict,'A')

    
    
             
main()
