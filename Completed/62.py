class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # base cases where only can go 1 direction
        M = [[1]*(m+1)]*(n+1)
        
        for i in range(2, n+1):
            for j in range(2, m+1):
                M[i][j] = M[i-1][j] + M[i][j-1]

        return M[n][m]
        