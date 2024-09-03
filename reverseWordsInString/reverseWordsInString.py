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


