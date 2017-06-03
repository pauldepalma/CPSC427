
'''
make_tree is a python program that creates a dict rep. of a tree from a data
file
'''
from make_tree import *
'''
minimax:
Win for max: 1000
Win for min: -1000
'''
def minimax(tree,leaf, start,node_type):
    #start is a leaf node and will have a value
    if start[0] == 'L':
        return leaf[start]
    #max's turn
    if node_type == '+':
        #worst max can do
        v = -1000
        children = tree[start]
        for child in children:
            node_type = switch_type(node_type)
            v_tmp = minimax(tree,leaf,child,node_type)
            if v_tmp > v:
                v = v_tmp
        return v
    #min's turn
    if node_type == '-':
        #worst min can do
        v = 1000
        children = tree[start]
        for child in children:
            node_type = switch_type(node_type)
            v_tmp = minimax(tree,leaf,child,node_type)
            if v_tmp < v:
                v = v_tmp
        return v
            
            

    
def switch_type(node_type):
    if node_type == '+':
        return '-'
    return '+'

def main():
    tree_dict, leaf = make_tree("treeLeaf1.inp")
    value = minimax(tree_dict,leaf, 'A','+')
    if value == 1000:
        print "max wins"
    if value == -1000:
        print "min wins"

    
    
             
main()
