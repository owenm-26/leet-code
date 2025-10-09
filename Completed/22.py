class Solution:
    def generateParenthesis(self, n):
        
        # n=1
        # ["()"]
        # n=2
        # ["(())", "()()"]
        # n=3
        # ["((()))", "(()())", "(())()", "()(())", "()()()"]

        stack = []
        ans = []
        
        def backtrack(openN, closedN):
            # Base Case: Completed
            if (n == openN == closedN):
                ans.append("".join(stack))
                opened, closed = 0,0 
            
            # At max of opened
            if openN < n:
                stack.append("(")
                backtrack(openN+1, closedN)
                stack.pop() # clean up the shared stack

            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN+1)
                stack.pop()

        backtrack(0,0)

        return ans

