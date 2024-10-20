# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        # explanation: Run BFS and then iterate through each level and take the last node added to each layer

        layers = {}
        dist = {root: 0}
        parents = {root: None, None: 0}

        def bfs(root):
            if root:
                dist[root] = dist[parents[root]] + 1

               
                if parents[root] in layers:
                    layers[dist[root]].append(root)
                else:
                    layers[dist[root]] = [root]
                if root.left:
                    parents[root.left] = root
                if root.right:
                    parents[root.right] = root
                bfs(root.left)
                bfs(root.right)
        if root:
            layers[0] = [root]
            if root.left:
                parents[root.left] = root
                bfs(root.left)
            if root.right:
                parents[root.right] =root
                bfs(root.right)
                
        rightMost =[]
        for l in layers:
            rightMost.append(layers[l][-1].val)
        return rightMost
            
        