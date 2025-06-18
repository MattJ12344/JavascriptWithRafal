class Solution(object):
    def maxProfit(self, prices : List[int]) ->  int:
        """
        :type prices: List[int]
        :rtype: int
        """
        buyPrice:int = prices[0]
        profit:int = 0

        for p in prices[1:]:
            if buyPrice > p:
                buyPrice = p
            
            profit = max(profit, p - buyPrice)
        
        return profit