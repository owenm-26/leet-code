class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # explanation: Split into 2 groups and run House Robber 1. First group is 1 go n-1, second is 2 to n

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        def findBest(numSlice):
            if len(numSlice) < 3:
                return max(numSlice)
            nSlice = len(numSlice)
            dp = {}
            dp[0] = numSlice[0]
            dp[1] = max(numSlice[0], numSlice[1])

            for i in range(2, nSlice):
                dp[i] = max(dp[i-1], dp[i-2] + numSlice[i])
        
            return dp[nSlice-1]

        first = nums[:n-1]
        last = nums[1:]
        print(first, last)

        firstBest = findBest(first)
        lastBest = findBest(last)

        print(firstBest, lastBest)

        return max(firstBest, lastBest)
        
