class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        
        if x == 0:
            return 0

        answer = x
        
        pow_num = abs(n)

        if pow_num > 1:
            for i in range(n - 1):
                answer *= x
        
        return answer if n > 0 else 1/answer


print(Solution().myPow(5, 2))