"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        def qtree(r1, r2, c1, c2):
            if r1 == r2 and c1 == c2:
                return Node(grid[r1][c1], True, None, None, None, None)
            
            cur = Node(False, False)
            mr = (r2+r1) // 2
            mc = (c2 +c1) // 2
            cur.topLeft = qtree(r1, mr, c1, mc)
            cur.topRight = qtree(r1, mr, mc+1, c2)
            cur.bottomLeft = qtree(mr+1, r2, c1, mc)
            cur.bottomRight = qtree(mr+1, r2, mc+1, c2)

            if (cur.topLeft.isLeaf and cur.topRight.isLeaf and 
            cur.bottomLeft.isLeaf and cur.bottomRight.isLeaf 
            and cur.topLeft.val == cur.topRight.val == 
            cur.bottomLeft.val == cur.bottomRight.val):
                cur.isLeaf = True
                cur.val = cur.topLeft.val
                cur.topLeft = cur.topRight = cur.bottomLeft = cur.bottomRight = None
            else:
                cur.isLeaf = False
                cur.val = 1
            return cur

        return qtree(0, len(grid)-1, 0, len(grid)-1)           
            