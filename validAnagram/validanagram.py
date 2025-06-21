class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        freqDict = {}

        if len(s) != len(t):
            return False
      
        for letter in s:
            if letter not in freqDict:
                freqDict[letter] = 1
            else:
                freqDict[letter] += 1
        
        for letter in t:
            if letter not in freqDict:
                return False
            freqDict[letter] -= 1
        
        for key in freqDict.keys():
            if freqDict[key] != 0:
                return False
        return True
        
