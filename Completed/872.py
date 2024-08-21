# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """

        # explanation: Run dfs on both trees and catch the nodes with no kids. 
        #Look at left kid first

        leafs={}
        leafs[0] = [] #tree1
        leafs[1] = [] #tree2

        visited = set()

        stack = []
        stack.append(root1)

        while len(stack) != 0:
            node = stack.pop()
            if node in visited:
                continue
            if node.left:
                stack.append(node.left)
            visited.add(node)
            if node.right:
                stack.append(node.right)
            elif not node.left and not node.right:
                leafs[0].append(node.val)
        
        visited = set()
        stack.append(root2)
        while len(stack) != 0:
            node = stack.pop()
            if node in visited:
                continue
            visited.add(node)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            elif not node.left and not node.right:
                leafs[1].append(node.val)

        return leafs[0] == leafs[1]
