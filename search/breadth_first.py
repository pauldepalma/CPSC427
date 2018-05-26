import pickle

#reads in a tree represented as a dictionary and serialized/stored with pickle
def get_tree(file):
    tree = pickle.load(open(file,'rb'))
    return tree


def breadth_first(tree,root):
    visited = []
    queue = [root]
    while queue: #returns true if list has items, false otherwise
        vertex = queue.pop(0) #dequeue
        if vertex not in visited:
            visited.append(vertex)
            children = tree[vertex]
            for item in children:
                if item not in visited:
                    queue.append(item)       
    return visited
 

def main():
    file = "tree.p"

    tree = get_tree(file)
    root = 'A'

    print(breadth_first(tree,root))
    
    
             
main()
