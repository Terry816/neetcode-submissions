class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        rank = [1] * n
        self.components = n

        def find(n):
            if n != parent[n]:
                parent[n] = find(parent[n])
            return parent[n]
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1 == p2:
                return False

            self.components -= 1
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                rank[p2] += rank[p1]
                parent[p1] = p2
            return True
        
        for u,v in edges:
            if not union(u,v):
                return False

        return True if self.components == 1 else False
            

