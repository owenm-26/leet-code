class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        # explanation: add to stack until you hit ']' once you hit that undo the stack and
        # store in a 'copy' string until you hit '[' remove it and then store the number(s) 
        # before it as 'multipliers' then multiply 'copy' and add to stack

        stack = []

        for char in s:
            
            # a regular character
            if char != ']':
                stack.append(char)
                continue
            
            copy = ""
            while stack and stack[-1] != '[':
                copy = stack.pop() + copy
            stack.pop() # get rid of '['

            multiplier = ""
            while stack and stack[-1].isnumeric():
                multiplier = stack.pop() + multiplier
            
            stack.append(int(multiplier) * copy)
        
        return ''.join(stack)