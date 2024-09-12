class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for x in range(0, len(nums)):
            complement = target - nums[x]
            if complement in hashMap:
                return [hashMap[complement], x]
            else:
                hashMap[nums[x]] = x
        return [-1,-1]
        
