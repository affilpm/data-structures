class Graph:
    def __init__(self, directed=True) -> None:
        self.graph = {}  # A dictionary to store the graph
        self.directed = directed  # Flag to determine if the graph is directed
        
    def add_node(self, node):
        """Add a node to the graph."""
        if node not in self.graph:
            self.graph[node] = []
    
    def add_edge(self, node1, node2, weight=None):
        """Add an edge between node1 and node2 with an optional weight."""
        if node1 not in self.graph:
            self.add_node(node1)
        if node2 not in self.graph:
            self.add_node(node2)
        
        # For directed graphs, we add the edge in one direction
        self.graph[node1].append((node2, weight))  # Append as tuple (node2, weight)

        # For undirected graphs, also add the reverse edge if needed
        if not self.directed:
            self.graph[node2].append((node1, weight))  # Add reverse edge

    def bfs(self, start):
        """Perform BFS starting from the given node."""
        visited = set()
        queue = [start]  # Queue to keep track of nodes to visit
        
        visited.add(start)
        
        while queue:
            node = queue.pop(0)  # Pop the first node
            print(node, end=" ")  # Print the current node
            
            # Add unvisited neighbors to the queue
            for neighbor, weight in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    
    def dfs(self, start, visited=None):
        """Perform DFS starting from the given node."""
        if visited is None:
            visited = set()
        
        visited.add(start)
        print(start, end=" ")  # Print the current node
        
        # Visit all unvisited neighbors
        for neighbor, weight in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

# Example usage:
g = Graph(directed=True)  # Create a directed graph
g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

print("BFS Traversal:")
g.bfs('A')  # Start BFS from node 'A'

print("\nDFS Traversal:")
g.dfs('A')  # Start DFS from node 'A'