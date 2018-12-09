class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        direct_flag = False
        c_list = [list() for i in range(numRows)]

        if numRows == 1:
            return s

        start = 0
        for c in s:
            c_list[start].append(c)
            
            if not direct_flag:
                if start == numRows - 1:
                    direct_flag = True
                    start -= 1
                else:
                    start += 1
            
            else:
                if start == 0:
                    direct_flag = False
                    start += 1
                
                else:
                    start -= 1

        result = ""
        for row in c_list:
            for c in row:
                result += c
        
        return result

    
assert Solution().convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
assert Solution().convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
assert Solution().convert("ABC", 1) == "ABC"           
