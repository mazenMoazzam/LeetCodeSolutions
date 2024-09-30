import heapq
import collections

class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def countElements(array):
            freqCount= {}
            for x in array:
                if x in freqCount:
                    freqCount[x] += 1
                else:
                    freqCount[x] = 1
            return freqCount
        #decided to intialize a hashmap to count the frequencies for each element that will be inserted into the heap. O(n) time operation. O(n) space used, due to it scaling dependent
        #on the number of elements in the array.

        def topK(array, k):
            counter = countElements(array)
            heap = [(-freq, num) for num, freq in counter.items()] #as python does not provide maxHeaps, I decided to use a min heap and negate the frequencies,
            #as the minimum frequency will be still be the same value when it is a positive number. 
            heapq.heapify(heap)
            topElements = [heapq.heappop(heap)[1] for x in range(k)]

            return topElements
        return topK(nums, k) 
        
#runtime of code: O(N + m + k log m)
        
