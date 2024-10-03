def lastSquare(n, m , grid):

    # down, right, up, left
    directions = [(1,0), (0, 1), (-1, 0), (0,-1)]

    visitedSquares = [[False for _ in range(m)] for _ in range(n) ]

    x, y = 0,0
   
    visitedSquares[x][y] = True

    direction_count = 0
    hop_count = 0
    last_cell = grid[0][0]

    while True:
        running_x = x + directions[direction_count][0]
        running_y = y + directions[direction_count][1]

        if 0 <= running_x < n and 0 <= running_y < m and not visitedSquares[running_x][running_y]:
            hop_count += 1
            visitedSquares[x][y] = True
        
            if hop_count % 2 == 0:
                last_cell = grid[running_x][running_y]
            x = running_x
            y = running_y
                

        else:
            direction_count = (direction_count + 1) % 4
            running_x = x + directions[direction_count][0]
            running_y = y+ directions[direction_count][1]

            if not(0 <= running_x < n and 0 <= running_y < m and not visitedSquares[running_x][running_y]):
                break
    
    return last_cell


if __name__ == "__main__":
    n=3
    m=3
    grid=[[29, 8, 37], [15, 41, 3], [1,10,14]]
    print(lastSquare(n,m,grid))