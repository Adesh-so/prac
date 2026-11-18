from collections import deque


# Graph Representation using Adjacency List
class Graph:

    def __init__(self):
        self.graph = {}

    # Add an edge between two vertices
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []

        if v not in self.graph:
            self.graph[v] = []

        self.graph[u].append(v)
        self.graph[v].append(u)

    # Depth First Search (Recursive)
    def dfs(self, start, visited=None):

        if visited is None:
            visited = set()

        # Visit the current node
        visited.add(start)
        print(start, end=" ")

        # Visit all unvisited neighbours
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)

    # Breadth First Search (Iterative)
    def bfs(self, start):

        visited = set()
        queue = deque([start])

        visited.add(start)

        while queue:
            node = queue.popleft()

            print(node, end=" ")

            # Visit all unvisited neighbours
            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)


# Main Program
g = Graph()

# Adding edges to the undirected graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(3, 6)

# Perform DFS Traversal
print("DFS Traversal (Starting from node 0):")
g.dfs(0)

# Perform BFS Traversal
print("\nBFS Traversal (Starting from node 0):")
g.bfs(0)
