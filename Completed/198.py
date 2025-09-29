class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]

        M = [float("-inf")] * len(nums)
        M[0] = nums[0]
        M[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            M[i] = max(nums[i] + M[i-2], M[i-1])

        return M[-1]
        