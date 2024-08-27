# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
#problem asks to find the first bad version of software given n versions, given isBadVersion API to determine if a version is bad. 
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left, right = 1, n
        
        while left < right:
            mid = (left + right) // 2
            
            if isBadVersion(mid):
                right = mid  
            else:
                left = mid + 1 
    
        return left
#problem solution involving binary search algorithm. Time Complexity: O(log n) where n represents the number of versions. 
