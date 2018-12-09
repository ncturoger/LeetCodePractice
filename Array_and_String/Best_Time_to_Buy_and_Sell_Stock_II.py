class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices:
            min_buy = prices[0]
            max_profit = 0
            i = 1

            while i < len(prices):
                min_buy = min(prices[i], min_buy)
                max_profit = max(max_profit, i - min_buy)



assert Solution().maxProfit([7,1,5,3,6,4]) == 7
assert Solution().maxProfit([1,2,3,4,5]) == 4
assert Solution().maxProfit([7,6,4,3,1]) == 0
