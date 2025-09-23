class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        n = len(board)
        square_dimension = n/3

        # check rows are valid
        for row in range(n):
            seen_nums = set()
            for col in range(n):
                if board[row][col] == ".": continue
                if board[row][col] in seen_nums:
                    print('failing row-wise', row, col)
                    return False
                seen_nums.add(board[row][col])
        
        # check cols are valid
        for col in range(n):
            seen_nums = set()
            for row in range(n):
                if board[row][col] == ".": continue
                if board[row][col] in seen_nums:
                    print('failing col-wise', row, col)
                    return False
                seen_nums.add(board[row][col])
        
        # check squares are valid
        square_num = 0
        while square_num < n:
            print("-----")
            seen_nums = set()
            for row in range(3*(square_num/3), square_dimension+3*(square_num/3)):
                for col in range(3*(square_num % 3), square_dimension+3*(square_num % 3)):
                    print(row, col)
                    if board[row][col] == ".": continue
                    if board[row][col] in seen_nums:
                        print('failing square-wise', row, col)
                        return False
                    seen_nums.add(board[row][col])
                # reset vars and continue
            square_num +=1
                
        
        return True