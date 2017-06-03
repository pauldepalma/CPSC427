
'''
make_tree is a python program that creates a dict rep. of a tree from a data
file.  See make_tree for the format
'''
from make_tree import *
'''
recursive version of depth_first traversal
'''


#Returns a list with each node name and its value in pre-order order
def depth_firstR(tree,value,start,traverse,visited):
    #stopping case. Have encountered a leaf node. Append to list and return
    if tree[start] is None:
        traverse.append(str(start) + ':' + str(value[start]))
        return traverse

    visited.append(start)
    traverse.append(str(start) + ':' + str(value[start]))
    children = tree[start]
    for child in children:
        if child not in visited:
            visited.append(child)
            traverse = depth_firstR(tree,value,child,traverse,visited)
    return traverse


def main():
    tree_dict, value_dict = make_tree("tree.inp")
    traverse = [] #List of nodes visited
    visited = [] #Prevents processing a node more than one
    print depth_firstR(tree_dict,value_dict,'A',traverse,visited)
    
             
main()
