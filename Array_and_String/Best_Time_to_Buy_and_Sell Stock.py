class Solution(object):
    # Time Limit Exceeded
    def maxProfit_1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for idx, price in enumerate(prices):
            buy = price
            i = 1
            while idx + i < len(prices):
                profit = prices[idx + i] - buy
                if profit > max_profit:
                    max_profit = profit
                i += 1
        
        return max_profit

    # pass
    def maxProfit_2(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        if prices:
            min_p = prices[0]
            for i in range(1, len(prices)):
                if min_p < prices[i]:
                    max_profit = max(prices[i] - min_p, max_profit)
            
                else:
                    min_p = prices[i]
        
        return max_profit
