class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")

# Example usage:
g = Graph()
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 4)
g.display()
# Output:
# 1 -> [2, 3]
# 2 -> [1, 4]
# 3 -> [1]
# 4 -> [2]
