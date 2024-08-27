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

        def topK(array, k):
            counter = countElements(array)
            heap = [(-freq, num) for num, freq in counter.items()]
            heapq.heapify(heap)
            topElements = [heapq.heappop(heap)[1] for x in range(k)]

            return topElements
        return topK(nums, k) 
#runtime of code: O(N + m + k log m)
        
