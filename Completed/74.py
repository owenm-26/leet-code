class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def binary_search(flat_matrix: List) -> bool:
            length = len(flat_matrix)
            mid = length // 2
            
            # Case 0: DNE
            if length == 0:
                return False
                
            # Case 1: Need to move right
            if flat_matrix[mid] < target:
                return binary_search(flat_matrix[mid+1:])
            
            # Case 2: Need to move left
            elif flat_matrix[mid] > target:
                return binary_search(flat_matrix[:mid])
            
            else: # flat_matrix[mid] == target
                return True

        flat_matrix = matrix[0]
        for i in range(1,len(matrix)):
            flat_matrix.extend(matrix[i])

        return binary_search(flat_matrix=flat_matrix)




    """
    target = 10
    flat_matrix = [1,2,4,8,10,11,12,13,14,20,30,40]
    length = 12
    mid = 6
    --
    target = 10
    flat_matrix = [1,2,4,8,10,11]
    length = 6
    mid = 3
    --
    target = 10
    flat_matrix = [10,11]
    length = 2
    mid = 1
    --
    target = 10
    flat_matrix = [10]
    length = 1
    mid = 0
    --
    """