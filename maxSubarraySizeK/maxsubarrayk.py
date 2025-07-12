#User function Template for python3
class Solution:
    def maximumSumSubarray (self,arr,k):
        # code here 
        maxSum = 0
        left = 0
        windowSum = 0
        
        for right in range(len(arr)):
            windowSum += arr[right]
            
            if right >= k - 1: #used to see if the curr array reaches the size K
                maxSum = max(maxSum, windowSum) #comparing maxSum to currSum and redefining before we subtract and move on 
                windowSum -= arr[left]
                left += 1
            
        return maxSum




#Sliding window approach. With window sum being added regardless in loop and decrement when it reaches K length after comparing maxSum and window Sum and redefining.
#Time: O(n)
#Space: constant
