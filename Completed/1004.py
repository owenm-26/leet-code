class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # explanation: iterate through list once and use all the zeroes you can
        # before moving the front to past the first zero and try again.
        
        zeroesUsed = 0
        best = 0
        i=0
        start = 0

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroesUsed += 1
            while zeroesUsed > k:
                if nums[start] == 0:
                    zeroesUsed -= 1
                start += 1
            
            best = max(best, i-start+1)
        
        return best
