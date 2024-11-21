
class Solution(object):

    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        anagrams = {}

        for e in strs:
            sorted_e = ''.join(sorted(e))
            if sorted_e in anagrams:
                anagrams[sorted_e] += [e]
            else:
                anagrams[sorted_e] = [e]
        
        return anagrams.values()

        

        # for e in strs:
        #     sig = [0] * 26
            
        #     for letter in e:
        #         sig[ord(letter) - ord('a')] +=1
        #     sig= ''.join(str(x)+'#' for x in sig)

        #     if sig in anagrams:
        #         anagrams[sig] += [e]
        #     else:
        #         anagrams[sig] = [e]

        # return anagrams.values()
        