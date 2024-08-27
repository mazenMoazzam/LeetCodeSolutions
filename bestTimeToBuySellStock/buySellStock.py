class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minPrice = float("inf") #intialized minPrice to a very large value so it is smaller than every value in the prices array ("inf" stands for infinity). 
        maxProfit = 0

        for stockPrice in prices:
            if stockPrice < minPrice: 
                minPrice = stockPrice
            currentProfit = stockPrice - minPrice

            if currentProfit > maxProfit: 
                maxProfit = currentProfit
        return maxProfit

#Time Complexity: This functions runs in linear time (O(n)) where n represents the number of days (or the length of the prices array). 
#Space Complexity: O(1) algorithm uses a fixed amount of extra space. 

        
