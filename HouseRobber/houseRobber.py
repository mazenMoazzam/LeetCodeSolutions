class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        dp0 = nums[0]
        dp1 = max(nums[0], nums[1])

        for x in range(2, len(nums)):
            current = max(dp1, nums[x] + dp0)
            dp0 = dp1
            dp1 = current
        return dp1
