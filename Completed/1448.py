# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # explanation: traverse down each path using DFS recursively and count

        if not root:
            return 0
        
        def dfs(node, currBest):
            if not node:
                return 0
            add = 0
            
            if node.val >= currBest:
                currBest = max(currBest, node.val)
                add = 1
            return add + dfs(node.right, currBest) + dfs(node.left, currBest)


        return dfs(root, root.val)


        # if root == None:
        #     return 0
        
        # goodNodeCount = 0

        # stack = []
        # stack.append(root)

        # maxSeen = {}
        # maxSeen[root] = root.val

        # parents = {}
        # parents[root] = root
        # explored = set()


        # while len(stack) != 0:
        #     node = stack.pop()
        #     if node in explored:
        #         continue
        #     explored.add(node)

        #     prevMax = maxSeen[parents[node]]
        #     if node.val >= prevMax:
        #         goodNodeCount += 1
        #         maxSeen[node] = node.val
        #     else:
        #         maxSeen[node] = prevMax

        #     if node.left:
        #         stack.append(node.left)
        #         parents[node.left] = node
        #     if node.right:
        #         stack.append(node.right)
        #         parents[node.right] = node
        
        # return goodNodeCount
