from collections import defaultdict
class Solution(object):
    def findingUsersActiveMinutes(self, logs, k):
        """
        :type logs: List[List[int]]
        :type k: int
        :rtype: List[int]
        """
        
        activity = defaultdict(set)
        ans = [0] * k
        # populate 
        for uid, time in logs:
            activity[uid].add(time)

        for user in activity:
            ans[len(activity[user])-1] +=1

        return ans