class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagramMap = {}

        for string in strs:
            sortedString = ''.join(sorted(string))

            if sortedString not in anagramMap:
                anagramMap[sortedString] = [string]
            else:
                anagramMap[sortedString].append(string)
        
        return list(anagramMap.values())
            


#O(n) time, due to traversing through n elements in the list which represent the amount of strings.
