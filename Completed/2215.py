class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        # explanation: set difference

        set1 = set(nums1)
        set2 = set(nums2)

        answer = [set1-set2, set2-set1]
        return answer
        