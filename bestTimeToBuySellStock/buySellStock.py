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

#strategy here is a sliding window where we need to declare a maxProfit and a minimum
#price to we can maximize the amount of prodit we obtain. Once these are declared, we 
#iterate through the list of prices for the stock, and we want to check if the current 
#price for the stock is lower than what we currently have, if it is, we redefine the 
#the minmum price to ensure we can maximize our profit. Using this value, we can 
#take the minimum price and subtract it from the current price and see the profit we 
#obtain from selling that stock, from there, we check and compare with the maximum profit
#and redefine the value if it is greater than the current value, once the array iteration
#is done, we return that value.

#Why did I define the minimum price and maxProfit variable? This is because we need the minimum price tracker to determine the maximum profit we can make for 
#the stock each day reset the maximum profit variable. Defined the maximumProfit variable for the case of tracking the greatest profit earned and this value
#is compared with the current profit calculated each day. Max profit is returned at the end of the function.


        
