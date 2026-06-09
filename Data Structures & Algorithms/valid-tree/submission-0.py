class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        adj_mat = defaultdict(list)
        for s, e in edges:
            adj_mat[s].append(e)
            adj_mat[e].append(s)
        
        visited = set()
        def dfs(node, parent):
            visited.add(node)

            for nei in adj_mat[node]:
                if nei == parent:
                    continue
                if nei in visited:
                    return True
                if dfs(nei, node):
                    return True
            return False
        if dfs(0, -1):
            return False
        return n == len(visited)

            
        
        