class MinStack:

    def __init__(self):
        self.stack = []
        self.minimums = []
        
    def push(self, val):
        self.stack.append(val)
        if(len(self.minimums) > 0):
            self.minimums.append(min(self.minimums[-1], val))
        else:
            self.minimums.append(val)

    def pop(self):
        self.stack.pop()
        self.minimums.pop()
        
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minimums[-1]
