class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # explanation: iterate through list once and update first + second when 
        # you find a number <= to either of them. If you find a number that is 
        # <= both of them then that means you have found the increasing triplet since
        # you're iterating from left to right
        first = second = float('inf')

        for item in nums:
            if item <= first:
                first = item
            elif item <= second:
                second = item
            else:
                return True

        return False

        