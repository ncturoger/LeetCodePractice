class Solution:
    def romanToInt(self, s):
        roman_dic = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }        
        
        i = len(s) - 1
        last = None
        num = 0
        while i > -1:
            now = roman_dic[s[i]]
            if last:
                if last > now:
                    num -= now
                
                else:
                     num += now

            else:
                num += now
            
            last = now
            i -= 1
        return num


assert Solution().romanToInger("III") == 3
assert Solution().romanToInger("IV") == 4
assert Solution().romanToInger("IX") == 9
assert Solution().romanToInger("LVIII") == 58
assert Solution().romanToInger("MCMXCIV") == 1994