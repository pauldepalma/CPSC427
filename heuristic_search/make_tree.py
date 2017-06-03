'''
Reads a file and constructs two dictionary:
tree_dict: each key is a node with values that are its children.
Leaf nodes have value None.
value_dict: each node is a key whose value is the value of the node.

File Format:
Parent nodes and children are separated by commas
A,B,C,C indicates that A is a parent with B,C,D its children
Leaf nodes are followed by a semi-colon
F; indicates that F is a leav node

Every node must have a value
A:0  indicates that A has a value of 0
'''

def make_tree(tree_in):
    tree = open(tree_in,'r')
    tree_string = tree.read().rstrip()
    tree.close();
    
    tree_list = tree_string.split('\n')
    tree_dict = {}
    value_dict = {}
    for line in tree_list:
        if line[1] == ':':
            line = line.split(':')
            value_dict[line[0]] = int(line[1])
        else:
            if line[1] == ';':
                tree_dict[line[0]] = None
            else:
                tree_dict[line[0]] = [line[i] for i in range(1,len(line)) if line[i] != ',']
            
    return tree_dict, value_dict
'''
def main():
    a,b = make_tree("tree.inp")


main()
'''


