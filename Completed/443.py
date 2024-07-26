class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        # explanation: iterate through keep track of streak and letter
        # and append once you hit a new letter before writing back to char

        if(len(chars) == 0):
            return 0
        
        streak = 1
        char = chars[0]
        answer = [char]

        for c in chars[1:]:
            if(c == char):
                streak = streak + 1
            else:
                if(streak != 1):
                    for d in str(streak): 
                        answer.append(d)
                       
                streak = 1
                answer.append(c)
                char = c
        if(streak != 1):
            for d in str(streak):
                      
                        answer.append(d)
        for i in range(len(answer)):
            chars[i] = answer[i]
        chars = chars[:len(answer)]
        return len(chars)
        