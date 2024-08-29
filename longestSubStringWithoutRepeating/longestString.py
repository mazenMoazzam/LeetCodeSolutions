class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        #A for loop could work this implementation, have a constant "live" string 
        #if the current character about to be added is not in current string, then add it, 
        #However, if it is, then reset string and add the current string. (Scraped solution)

        #Update: a sliding window approach is much easier and suited for this problem. 
        #Intialized a start var, and a set to keep track of the non-reoccuring characters,
        #maxLength will always be at zero at the start iterate through the string, add
        #the characters to the set and update the max length, if the while condition is met,
        #meaning a character is already in the set (start over), remove it from the set and 
        #close the window by incrementing the start pointer. Return the max length at the 
        #end of the function. 

        #Time Complexity: O(n) or linear where n is the length of the input string, 
        #making this code efficient for larger inputs. 

        characterSet = set()
        start = 0
        maxLength = 0

        for end in range(len(s)): 
            while s[end] in characterSet: 
                characterSet.remove(s[start])
                start += 1
            characterSet.add(s[end])
            maxLength = max(maxLength, end - start + 1)
        return maxLength

        

        
