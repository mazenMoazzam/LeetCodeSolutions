class MyStack(object):

    def __init__(self):
        self.__stackList = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.__stackList.insert(0,x)
        

    def pop(self):
        """
        :rtype: int
        """
        element = self.__stackList.pop(0)
        return element
        

    def top(self):
        """
        :rtype: int
        """
        return self.__stackList[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        if len(self.__stackList) == 0:
            return True
        else: 
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
