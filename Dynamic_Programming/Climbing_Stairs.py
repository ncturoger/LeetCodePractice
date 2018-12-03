class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        step = 0
        for i in range(0, n+1):
            if (n-i) % 2 == 0:
                y = int((n-i) / 2)
                step += int(self.stage(i+y) / (self.stage(i) * self.stage(y)))
        
        return step
    
    def stage(self, num):
        result = 1
        for i in range(1, num + 1):
            result *= i
        return result


print(Solution().climbStairs(2))