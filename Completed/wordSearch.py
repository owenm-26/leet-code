def isWordInGrid(word, grid):

    def isVertical(word, cols):
        word = word.lower()
        for col in cols:
            str = ''.join(col)
            if word in str.lower():
                return True
        
        return False
    
    verticals = [[] for _ in range(len(grid[0]))]
    diagonalLeft =  [''] 
    diagonalRight = [''] 

    # check rows for word
    for row in grid:
        str = ''.join(row)
        if word in str:
            return True
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # left diagonal
            if i == j:
                diagonalLeft.append(grid[i][j])

            if i+j == len(grid)-1:
                diagonalRight.append(grid[i][j])
            
            # every item is part of a col
            verticals[j].append(grid[i][j])
    
    return isVertical(word, verticals) or word in ''.join(diagonalLeft).lower() or word in ''.join(diagonalRight).lower()


if __name__ == "__main__":
    word = 'CAT'
    grid = [['C', 'A', 'T']]
    grid2 = [['C', 'O', 'T'], ['a', 't', 'p'], ['T', 'p','w']]

    print(isWordInGrid(word, grid2))