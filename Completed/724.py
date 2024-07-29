class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # explanation: prefix sum and ignore number currently on

        # sum all elements of array
        total = 0
        for e in nums:
            total += e
        
        # create a left sum and check if equal to right sum
        leftSum = 0
        for i in range(len(nums)):
            num = nums[i]
            if(leftSum == total - leftSum-num):
                return i
            leftSum += num
        
        return -1
            