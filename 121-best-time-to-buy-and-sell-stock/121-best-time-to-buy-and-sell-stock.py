class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        maxProfit = 0
        buyDayPrice = prices[0]
        sellDayPrice = prices[0]
        
        for val in prices:
            if(val < buyDayPrice):
                buyDayPrice = val
                sellDayPrice = val
            if(val > sellDayPrice):
                sellDayPrice = val
            if(sellDayPrice - buyDayPrice > maxProfit):
                maxProfit = sellDayPrice - buyDayPrice
        
        return maxProfit
        
        