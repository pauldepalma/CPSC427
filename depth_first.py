def depth_first(graph, start):
    visited = []
    stack = [start]
    while stack: #returns true if list has items, false otherwise
        vertex = stack.pop() #remove the most recently added item
        if vertex not in visited:
            visited.append(vertex)
            children = graph[vertex]
            children.reverse() #add right to left, e.g. ['Q','C','B']
            for item in children:
                if item not in visited:
                    stack.append(item)       
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
              
    print depth_first(graph,'A')

    
    
             
main()
