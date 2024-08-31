class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backTrack(start, currentSubset):
            result.append(list(currentSubset))
            for i in range(start, len(nums)):
                currentSubset.append(nums[i])
                backTrack(i + 1, currentSubset)
                currentSubset.pop()
        result = []
        backTrack(0, [])
        return result
        
