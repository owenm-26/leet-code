# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # explanation: work bottom up and keep track of 2 variables (height, diameter)
        # height is 1 + max(left, right) and diameter is 2 + left + right. Runs in O(n)
        
        result = [0]

        def dfs(root):
            if root is None:
                return -1
            
            left = dfs(root.left)
            right = dfs(root.right)

            # diameter = 2 + left height + right height
            result[0] = max(result[0], 2 + left + right)

            return 1 + max(left, right)

        dfs(root)
        return result[0]
        

        