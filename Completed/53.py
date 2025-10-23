class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [float("-inf")]* (len(nums)+1)

        for i in range(1, len(dp)):
            dp[i] = max(nums[i-1], dp[i-1] + nums[i-1])
        
        return max(dp)

        