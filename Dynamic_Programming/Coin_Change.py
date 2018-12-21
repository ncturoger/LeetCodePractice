class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [0 for i in range(amount+1)]

        for i in range(amount):
            search = amount - dp[i-1]
