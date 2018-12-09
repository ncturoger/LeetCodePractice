class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        
        gcd = self.GCD(x, y)
        if gcd == 0:
            return False
        
        
        if z == 0 or z % gcd == 0 and x + y >= z:
            return True
        
        else:
            return False
    

    def GCD(self, a, b):
        c = max(a, b)
        d = min(a, b)

        if d == 0:
            return c
        
        if c % d == 0:
            return d
        
        else:
            return self.GCD(d, c % d)