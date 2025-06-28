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
#General approach is to create a dictionary which the key will represent the string sorted in order, which will help distinguish what string is an anagram or not
#with this, we travrse through the list to sort the current string, we check if this string is in the anagram dictionary, if it is, we simply add it to the list value
#of the dictionary, if not er vreate a list with the first element being the current iteration of the string.
