class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        from collections import defaultdict
        adj_mat = defaultdict(list)
        for s, e in edges:
            adj_mat[s].append(e)
            adj_mat[e].append(s)
        
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)

            for nei in adj_mat[node]:
                if nei == parent:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        return dfs(0, -1) and n == len(visited)

            
        
        