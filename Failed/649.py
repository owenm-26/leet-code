from collections import deque
class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        # explanation: use deque for faster left pop and compare the front of queue
        # for both dire and radiant. Pick the first one as the one that votes
        # the other out and add the first one to the end of the queue

        direIndicies = deque()
        radiantIndicies = deque()
        n = len(senate)
        for i in range(n):
            if senate[i] == 'D':
                direIndicies.append(i)
            else:
                radiantIndicies.append(i)

        while direIndicies and radiantIndicies:
            d = direIndicies.popleft()
            r = radiantIndicies.popleft()

            if r > d:
                direIndicies.append(n + d)
            else:
                radiantIndicies.append(n + r)
        
        return 'Radiant' if radiantIndicies else 'Dire'

        




        