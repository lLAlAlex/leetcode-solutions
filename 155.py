class MinStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val):
        self.stack.append(val)
        
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self):
        popped = self.stack.pop()
        
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        
    def printStack(self):
        return self.min_stack
    
obj = MinStack()
obj.push(-2)
obj.push(-2)
obj.push(-3)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.getMin())