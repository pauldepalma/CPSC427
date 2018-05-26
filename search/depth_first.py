import pickle

#reads in a tree represented as a dictionary and serialized/stored with pickle
def get_tree(file):
    tree = pickle.load(open(file,'rb'))
    return tree

def depth_first(tree):
    visited = []
    stack = ['r']
    while stack: #returns true if list has items, false otherwise
        vertex = stack.pop() #remove the most recently added item
        if vertex not in visited:
            visited.append(vertex)
            children = tree[vertex]
            children.reverse() #add right to left, e.g. ['Q','C','B']
            for item in children:
                if item not in visited:
                    stack.append(item)       
    return visited

        

def main():
    
    file = "tree.p"

    tree = get_tree(file)

    print(depth_first(tree))
    
             
main()
