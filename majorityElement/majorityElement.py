class Solution(object):
    def majorityElement(self,nums):
        newList = []
        if len(nums) == 1:
            return nums[0]
        else:
            for x in nums:
                occurance =  nums.count(x)
                if occurance >= 2:
                    newList.append(x)
            return newList[0]
