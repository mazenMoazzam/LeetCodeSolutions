class MinStack(object):

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.stack.append(val)

        if not self.minStack or val <= self.minStack[-1]: 
            self.minStack.append(val) 
      
    def pop(self):
        """
        :rtype: None
        """
        if self.stack: 
            val = self.stack.pop()
            if val == self.minStack[-1]: 
                self.minStack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack: 
            return self.stack[-1]
        return None
        
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack: 
            return self.minStack[-1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
