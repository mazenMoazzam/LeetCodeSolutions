class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashMap = {}
        
        for i, num in enumerate(nums):
            if num in hashMap:
                if abs(i - hashMap[num]) <= k:
                    return True
            hashMap[num] = i

        return False

        #Solution runs in linear time O(n), due to the fact that using num and i, has to go through 
        #each of the elements of the lists, nums.
