from typing import Counter

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # transpose the grid so that we get columns
        columnOccurrences = Counter(zip(*grid))
        rowOccurrences = Counter(map(tuple,grid))
        
        # find the pairs, doing columns * rows for occurrences
        count = 0
        for key in rowOccurrences:
            if columnOccurrences[key] != None:
                count += columnOccurrences[key] * rowOccurrences[key]
        return count
        
    
    
    # not optimal
    def equalPairs(self, grid):
        columns = []
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if(len(columns)-1 < c):
                    columns.append([grid[r][c]])
                else:
                    columns[c].append(grid[r][c])
                
        count = 0
        for r in grid:
            for c in columns:
                if( r == c ):
                    count+=1
        return count