class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        nonZeroIndexes = []
        for i in range(len(nums)):
            if(nums[i] != 0):
                nonZeroIndexes.append(i)
        
        for i in range(len(nonZeroIndexes)):
            nums[i] = nums[nonZeroIndexes[i]]
        
        for j in range(len(nums) - len(nonZeroIndexes),0,-1):
            print(j)
            nums[-j] = 0

        return nums
