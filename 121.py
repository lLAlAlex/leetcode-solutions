class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        buy = prices[0]
        
        for price in prices:
            if price - buy > profit:
                profit = price - buy
            if buy > price:
                buy = price
        
        return profit
    
obj = Solution()
print(obj.maxProfit([10,1,5,6,7,1]))