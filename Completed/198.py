def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)

        if n < 3:
            return max(nums)

        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        temp = 0

        for i in range(2, n):
            temp = prev1
            prev1 = max(prev1, prev2 + nums[i])
            prev2 = temp
        return prev1
