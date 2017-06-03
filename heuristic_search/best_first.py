#a work in progress

def best_first(graph, start):
    visited = []
    queue = [start]
    while queue: #returns true if list has items, false otherwise
        vertex = queue.pop(0) #dequeue
        if vertex not in visited:
            visited.append(vertex)
            children = graph[vertex]
            for item in children:
                if item not in visited:
                    queue.append(item)       
    return visited
 

def main():
    graph = {'C' : ['A', 'D', 'E'],
             'A' : ['P', 'B'],
             'D' : ['R','42'],
             'E' : ['T', 'V'],
             'P' : ['2','3'],
             'B' : ['5', '100'],
             'R' : ['0'],
             'T' : ['2','1'],
             'V' : ['9', '11'],
             'q' : [],
             '0' : [],
             '1' : [],
             '2' : [],
             '3' : [],
             '5' : [],
             '9' : [],
             '11': [],
             '42': [],
             '100': []}
              
    print best_first(graph,'C')

    
    
             
main()
