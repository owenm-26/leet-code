class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        seen = set() 
        count = 0
        m = len(grid)
        n = len(grid[0])

        # iterate through grid, if hit one run dfs
            # add every seen 1 coordinate to a set
            # add 1 to counter everytime dfs started

        def dfs(i, j):
            if (i, j) in seen or i < 0 or j < 0 or i >= m or j >= n or grid[i][j] != "1":
                return
            seen.add((i,j))

            
            dfs(i-1,j)
        
            dfs(i+1,j)
        
            dfs(i, j-1)
        
            dfs(i, j+1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r,c) not in seen:
                    count +=1
                    dfs(r, c)

        return count
        