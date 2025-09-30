class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {'+', '-', '*', '/'}

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                val = -1

                match token:
                    case '+':
                        val = operand1 + operand2
                    case '-':
                        val = operand1 - operand2
                    case '*':
                        val = operand1 * operand2 
                    case '/':
                        val = (int(float(operand1) / operand2))
                    case _:
                        print(f"Invalid Operator: {token}") 

                stack.append(val)
        return stack.pop()




        