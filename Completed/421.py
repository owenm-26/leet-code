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
        """Invariant: grid is nxn"""
        
        if len(grid) == 0:
            return None
        # print(f"Running construct on grid size {len(grid)} x {len(grid[0])}")
        # print(grid)
        root = Node(0, 1, None, None, None, None)
       
        if(self.gridIsAllSame(subGrid=grid)):
            root.val = grid[0][0]
            root.isLeaf = True
        else:
            root.isLeaf = False
            root.val = 4 # not 0 or 1 (could be any value)
            self.divideGridIntoFour(node=root, subGrid=grid)
        
        return root
    
    def gridIsAllSame(self, subGrid: List[List[int]]) -> bool:
        """Whether the sub-grid contains the same number"""
        # O(n^2)
        first = subGrid[0][0]
        for r in range(len(subGrid)):
            for c in range(len(subGrid[0])):
                if subGrid[r][c] != first:
                    return False
        return True

    def divideGridIntoFour(self, node, subGrid:List[List[int]]) -> None:
        """Sets topLeft, topRight, bottomLeft, bottomRight recursively by calling construct"""
        mid = len(subGrid) // 2

        top_rows = subGrid[:mid]
        bottom_rows = subGrid[mid:]

        node.topLeft = self.construct(grid=[row[:mid] for row in top_rows])
        node.topRight = self.construct(grid=[row[mid:] for row in top_rows])
        node.bottomLeft = self.construct(grid=[row[:mid] for row in bottom_rows])
        node.bottomRight = self.construct(grid=[row[mid:] for row in bottom_rows])




        