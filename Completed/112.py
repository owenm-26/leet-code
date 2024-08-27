# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False
        
        targetSum -= root.val

        if not root.left and not root.right:
            return targetSum == 0
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


        # if not root:
        #     return False

        # leafSums = {}
        # leafSums[root] = root.val

        # parents = {}
        # parents[root] = None

        # leaves = []
        # def dfs(node, leafSums, parents, leaves):
            
        #     leafSums[node] = node.val + leafSums[parents[node]]
        #     if node.left:
        #         parents[node.left] = node
        #         dfs(node.left, leafSums, parents, leaves)
        #     if node.right:
        #         parents[node.right] = node
        #         dfs(node.right, leafSums, parents, leaves)
        #     if not node.left and not node.right:
        #         leaves.append(node)
        #         return
        # if root.left:
        #     parents[root.left] = root
        #     dfs(root.left, leafSums, parents, leaves)
        # if root.right:
        #     parents[root.right] = root
        #     dfs(root.right, leafSums, parents, leaves)
        # elif not root.left and root.val == targetSum:
        #     return True
        # for l in leaves:
        #     if leafSums[l] == targetSum:
        #         return True
        # return False
        