class Solution:
    def GCD(self, a, b):
        c = max(a, b)
        d = min(a, b)

        if c % d == 0:
            return d
        
        else:
            return self.GCD(d, c % d)
    

print(Solution().GCD(120, 99))