class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """

        # explanation: Create a stack, if * then pop else push current char

        stack = []
        
        for st in s:
            if st == '*':
                stack.pop()
            else:
                stack.append(st)
        return ''.join(stack)

    
