from typing import Counter


class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # explanantion: track num occurrences in hash map then check if that is unique

        occurrences = {}
        counts = []

        for ele in arr:
            if ele in occurrences:
                occurrences[ele] += 1
            else:
                occurrences[ele] = 1
        for o in occurrences:
            if occurrences[o] in counts:
                return False
            else:
                counts += [occurrences[o]]
        return True
    
    # FANCY explanation: use Counter() and check if len of set == len of list
    def uniqueOccurrences(self, arr):
        return (len(set(Counter(arr).values())) == len(list(Counter(arr).values())))