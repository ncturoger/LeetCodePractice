class Solution(object):
    def intToRoman(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dic = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }

        roman_str = ""
        s = int(s)
        digit = 1
        while s > 0:
            d = s % 10
            if d != 0:
                if d < 4:
                    for i in range(d):
                        roman_str = roman_dic[digit] + roman_str

                elif d == 4:
                    roman_str = roman_dic[digit] + roman_dic[digit*5] + roman_str

                elif d < 9:
                    for i in range(d-5):
                        roman_str = roman_dic[digit] + roman_str
                    roman_str = roman_dic[digit*5] + roman_str            

                else:
                    roman_str = roman_dic[digit] + roman_dic[digit*10] + roman_str
            new_s = int(s/10)
            s = new_s
            digit *= 10

        return roman_str


assert Solution().romanToInt("3") == "III"
assert Solution().romanToInt("4") == "IV"
assert Solution().romanToInt("9") == "IX"
assert Solution().romanToInt("58") == "LVIII"
assert Solution().romanToInt("1994") == "MCMXCIV"
            
