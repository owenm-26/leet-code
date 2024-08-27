class Solution(object):
    def pathSum(self, root, targetSum):

        # explanation: dfs through the tree and if you find a valid leaf, add its path
        # to the answer
        def dfs(node, path):
            if not root:
                return []
            if not node.right and not node.left:
                if targetSum == sum(path + [node.val]):
                    res.append(path+[node.val])
                    return res
            if node.right:
                dfs(node.right, path + [node.val])
            if node.left:
                dfs(node.left, path + [node.val])
        
        res = []
        dfs(root, [])
        return res


        # if not root:
        #     return []

        # parents = {}

        # def getPathLeaves(node, targetSum, parents):
        #     targetSum -= node.val

        #     # If it's a leaf node and targetSum == 0, return the current node
        #     if not node.left and not node.right and targetSum == 0:
        #         return [node]

        #     results = []

        #     # Recurse on the left child
        #     if node.left:
        #         parents[node.left] = node
        #         left_results = getPathLeaves(node.left, targetSum, parents)
        #         if left_results:
        #             results.extend(left_results)

        #     # Recurse on the right child
        #     if node.right:
        #         parents[node.right] = node
        #         right_results = getPathLeaves(node.right, targetSum, parents)
        #         if right_results:
        #             results.extend(right_results)

        #     return results
        
        # parents[root] = None
        # winningLeaves = []
        
        # # Check both sides, but also check if root itself is a solution
        # if root.left:
        #     parents[root.left] = root
        #     leftAnswers = getPathLeaves(root.left, targetSum - root.val, parents)
        #     winningLeaves.extend(leftAnswers)

        # if root.right:
        #     parents[root.right] = root
        #     rightAnswers = getPathLeaves(root.right, targetSum - root.val, parents)
        #     winningLeaves.extend(rightAnswers)

        # if not root.left and not root.right and root.val == targetSum:
        #     return [[root.val]]
        
        # # Now construct the paths from the leaves to the root
        # paths = []
        # for leaf in winningLeaves:
        #     path = []
        #     while leaf:
        #         path.append(leaf.val)
        #         leaf = parents[leaf]
        #     paths.append(path[::-1])
        
        # return paths
