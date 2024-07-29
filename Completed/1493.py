class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # INEFFICIENT: explanation: same as Max Consecutive Ones III but k = 1 and you need
        # to account for the case where they are all ones as well as subtract one from the
        # end total because instead of flipping you delete
         
        zerosDeleted = 0
        best = 0
        start = 0

        for i in range(len(nums)):
            if(nums[i] == 0):
                zerosDeleted += 1
            while zerosDeleted > 1:
                if nums[start] == 0:
                    zerosDeleted -= 1
                start += 1
            best = max(best, i-start+1-1)

        if(zerosDeleted == 0):
            return len(nums) - 1
        else:
            return best
        
    # simple but "inefficient"
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        left = 0
        right = 0
        count = 0
        n = len(nums)
        best = 0

        while right < n:
            if nums[right] == 0:
                count += 1
            while count > 1:
                if nums[left] == 0:
                    count -= 1
                left += 1
            right += 1
            best = max(best, right-left-1)

        return best