class Solution:
    def checkInclusion(self, s1, s2):
        needed = {}
        l1 = len(s1)
        
        if l1 > len(s2):
            return False

        for s in s1:
            if s in needed:
                needed[s] +=1
            else:
                needed[s] = 1

        curr_window = {}

        # populate original set
        for i in range(l1):
            if s2[i] in curr_window:
                curr_window[s2[i]] +=1
            else:
                curr_window[s2[i]] = 1

        if needed == curr_window:
                return True

        for j in range(l1, len(s2)):
            to_remove = s2[j-l1]
            if curr_window[to_remove] == 1:
                del curr_window[to_remove]
            else:
                curr_window[to_remove] -=1
            to_add = s2[j]
            if to_add in curr_window:
                curr_window[to_add] +=1
            else:
                curr_window[to_add] = 1
            if needed == curr_window:
                return True
        
        return False


