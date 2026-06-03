class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        adj_list = {} # Dictionary to store adj list
        for i in range(n): # Initialize every nodes neighbor list to be an empty list initially
            adj_list[i] = []
        for u, v in edges: # Iterate through every edge
            adj_list[u].append(v) # Add v to u's list of neighbors
            adj_list[v].append(u) # Add u to v's list of neighbors (the edge between u and v is undirected/two-way)
        visited = set() # Set to keep track of all visited nodes
        result = 0
        for i in range(n): # Visit every unvisited node
            if i not in visited: # If current node hasn't been visited, it's a new component and launch DFS from it
                result += 1
                dfs(i) 
        return result