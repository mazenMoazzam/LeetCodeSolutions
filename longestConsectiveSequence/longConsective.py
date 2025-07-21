class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        setNums = set(nums)
        longest = 0

        for num in setNums:
            if num - 1 not in setNums:
                currentNum = num
                currStreak = 1

                while currentNum  + 1 in setNums:
                    currentNum += 1
                    currStreak += 1
                longest = max(longest, currStreak)
        return longest
