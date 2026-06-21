class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        visited = set()
        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1
        return result