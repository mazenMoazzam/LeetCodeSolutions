class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dictionary = {')': '(', '}': '{', ']': '['}
        stack = []

        for x in s: 
            if x in dictionary.values(): 
                stack.append(x)
            elif x in dictionary.keys(): 
                if stack and stack[-1] == dictionary[x]: 
                    stack.pop()
                else: 
                    return False
        return not stack

            
