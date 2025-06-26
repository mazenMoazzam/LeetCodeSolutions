#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        maxSum = 0
        left = 0
        windowSum = 0
        
        for right in range(len(arr)):
            windowSum += arr[right]
            
            if right >= k - 1:
                maxSum = max(maxSum, windowSum)
                windowSum -= arr[left]
                left += 1
            
        return maxSum




#Sliding window approach. With window sum being added regardless in loop and decrement when it reaches K length after comparing maxSum and window Sum and redefining.
#Time: O(n)
#Space: constant
