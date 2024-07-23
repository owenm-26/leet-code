class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # explanation: Pointers from each end and move the 
        # one that points to the smaller value towards middle until they cross

        currentBest = 0
        x=0
        y=0
        p1, p2 = 0, len(height)-1

    
        while p1 != p2:
            x = p2 - p1
            y = min(height[p1], height[p2])
            currentBest = max(x * y, currentBest)
            if(y == height[p1]):
                p1 +=1
            else:
                p2 -= 1

        return currentBest