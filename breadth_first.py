def breadth_first(graph, start):
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
    graph = {'A' : ['B', 'C', 'Q'],
             'B' : ['F'],
             'C' : ['D','E'],
             'D' : [],
             'E' : [],
             'F' : [],
             'Q' : ['R'],
             'R' : ['X','Z'],
             'X' : [],
             'Z' : []}
              
    print breadth_first(graph,'A')

    
    
             
main()
