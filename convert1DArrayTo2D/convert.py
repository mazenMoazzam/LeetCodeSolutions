class Solution(object):
    def construct2DArray(self, original, m, n):
        """
        :type original: List[int]
        :type m: int
        :type n: int
        :rtype: List[List[int]]
        """

        if len(original) != m * n:
            return []
        
        newList = []

        for x in range(m):
            startingIndex = x * n
            endingIndex = n + startingIndex
            newList.append(original[startingIndex:endingIndex])
        
        return newList

