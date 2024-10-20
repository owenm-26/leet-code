# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """

        # explanation: Run BFS and then sum every layer and return the index of the layer with the highest sum 

        def bfs(trav):
            dist[trav] = dist[parents[trav]] + 1

            if dist[trav] in levels:
                levels[dist[trav]].append(trav.val)
            else:
                levels[dist[trav]] = [trav.val]
            
            if trav.left:
                parents[trav.left]= trav
                bfs(trav.left)
            if trav.right:
                parents[trav.right] = trav
                bfs(trav.right)

        levels = {}
        dist = {}
        parents = {}
        parents[root] = None
        dist[root] = 0
        dist[None] = -1
        levels[0] = [root.val]

        if root:
            bfs(root)

        maxSum = [float('-inf'),-1]
        for l in levels:
            currSum = sum(levels[l])
            print(currSum, maxSum)
            if currSum > maxSum[0]:
                maxSum = [currSum, l]
        
        return maxSum[1] +1 

        