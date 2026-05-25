class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        rank = [1] * n
        parent = [i for i in range(n)]
        self.components = n
        def find(n):
            if parent[n] != n:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2: # have the same parent
                return False
            
            self.components -= 1
            if rank[p1] >= rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
            return True

        for u1, u2 in edges:
            if not union(u1, u2):
                return False
        
        return self.components == 1
