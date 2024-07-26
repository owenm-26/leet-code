class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # explanation: use a stack to add the starting parenthesis and
        # pop when they find their pair. Check at end that stack is empty

        # if empty it works
        if(len(s) == 0):
            return True

        # if first char is invalid fail
        if(s[0] not in '({['):
            return False

        # if not even number of strings it fails
        if(len(s) % 2 != 0):
            return False

        pairs = {'(': ')', '{': '}', '[':']'}
        stack = []
        stack.append(s[0])

        for i in range(1,len(s)):
            if(s[i] in '({['):
                stack.append(s[i])
            else:
                if(len(stack) == 0 or s[i] != pairs[stack[-1]]):
                    return False
                else:
                    stack.pop()
        return len(stack)== 0