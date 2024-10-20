class Solution(object):
    def canMakeArithmeticProgression(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # explanation:  sort in ascending order and iterate
        
        arr.sort()
        difference = arr[1] - arr[0]

        for i in range(1,len(arr)-1):
            if arr[i+1] - arr[i] != difference:
                return False

        return True
