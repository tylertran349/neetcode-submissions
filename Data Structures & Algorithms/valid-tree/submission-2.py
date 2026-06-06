class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)
        queue = deque([0])
        visited = set([0])
        while queue:
            level_size = len(queue)
            for i in range(level_size):
                curr_node = queue.popleft()
                visited.add(curr_node)
                for neighbor in adj_list[curr_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
        return len(visited) == n