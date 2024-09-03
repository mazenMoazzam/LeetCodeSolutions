class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strippedString = s.strip()

        words = strippedString.split()

        reversedWords = words[::-1]
 
        return " ".join(reversedWords)


#Time Complexity: O(n) where n represents the number of words. Space Complexity: O(n), as python strings are immutable, the string is changed and the split() function is the primary cause for the linear space. As it allocates an 
#array where it adds the words to the string which will eventually scale up depending on the number of words from the inputted string. 
