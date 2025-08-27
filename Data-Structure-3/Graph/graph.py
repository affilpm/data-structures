class Graph:
    def __init__(self, directed=True) -> None:
        self.graph = {}  
        self.directed = directed  
        
        
        
    def add_node(self, node):

        if node not in self.graph:
            self.graph[node] = []
    
    
    
    def add_edge(self, node1, node2, weight=None):
     
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
     
        self.graph[node1].append((node2, weight))  
  
        if not self.directed:
            self.graph[node2].append((node1, weight)) 



    def bfs(self, start):
        visited = set()
        queue = [start]  
        
        visited.add(start)
        
        while queue:
            node = queue.pop(0)  
            print(node, end=" ") 
            
            for neighbour, weight in self.graph[node]:
                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)
    
    
    
    def dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=" ")  
        
        for neighbor, weight in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)



g = Graph(directed=True)  
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

print("BFS Traversal:")
g.bfs('A')  

print("\nDFS Traversal:")
g.dfs('A')