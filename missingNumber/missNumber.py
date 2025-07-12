class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected = n * (n + 1) // 2
        actual = 0

        for x in nums:
            actual += x
        return expected - actual


#O(n) and constant space, as variables do not scale up during algorithm.
