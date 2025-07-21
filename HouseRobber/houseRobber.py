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
#Basic DP problem where we want to find the maximum amount of money we can steal from each house which is represent in nums.
#Defined dp0 to represent i - 2 and dp1 which equals i - 1. (houses before previous and previous house). These represent starting points, and will iterate
#to the third house till the end and see if we can skip the current house and take the previous house value, or take the current house and add that to the i - 2
# house, we take the max of both. To iterate to next houses, we reassign dp0 and dp1, dp0 = dp1 (which is now 2 houses down) and dp1 = current which is i - 1.
#We return dp1, which contains the max value of earnings.
