class Solution(object):
    def containsDuplicate(self, nums):
        duplicates = set(nums)
        lists = list(duplicates)
        if len(lists) != len(nums):
            return True
        else:
            return False
