# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Explanation: BFS and keep track of longest dist, root is dist 1

        if root == None:
            return 0
        
        # distances from root
        dist = {}
        dist[root] = 1
        longestDist = 1

        # parents of each node
        parents = {}
        parents[root] = None

        # layers of tree
        layers = {}
        layers[0] = []
        layers[0].append(root)
        i = 0

        while layers[i]:
            layers[i+1] = []
            for node in layers[i]:
                if node.left:
                    dist[node.left] = dist[node] + 1
                    longestDist = max(longestDist, dist[node.left])
                    parents[node.left] = node
                    layers[i+1].append(node.left)
                if node.right:
                    dist[node.right] = dist[node] + 1
                    longestDist = max(longestDist, dist[node.right])
                    parents[node.right] = node
                    layers[i+1].append(node.right)
            i += 1 
        return longestDist
        
            
