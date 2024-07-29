class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        #OPTIMAL
        # explanation: prefix sum and for each loop. Max of result array

        heights = [0]

        for g in gain:
            heights.append(g + heights[-1])
        
        print(heights)
        return max(heights)