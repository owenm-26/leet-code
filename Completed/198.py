class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # explanation: simple DP
        
        n = len(nums)
        
        if n < 3:
            return max(nums)
        
        M = [0] * n
        M[0] = nums[0]
        M[1] = max(nums[0], nums[1])

        for i in range(2, n):
            M[i] = max(M[i-1], M[i-2] + nums[i])

        return M[-1]