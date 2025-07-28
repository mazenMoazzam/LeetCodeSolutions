class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        max_prod = nums[0]
        min_prod = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, max_prod * num, min_prod * num)
            temp_min = min(num, max_prod * num, min_prod * num)
            
            max_prod = temp_max
            min_prod = temp_min
            
            result = max(result, max_prod)
