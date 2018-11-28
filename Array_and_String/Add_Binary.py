class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        round_up = False
        result = str(int(a) + int(b))
        output_result = ""
        i = 1
        while i <= len(result):
            digit = int(result[-i])
            if round_up:
                digit += 1

            if digit > 1:
                round_up = True
                output_result = str(int(digit) % 2) + output_result
                if i == len(result):
                    output_result = "1" + output_result
            
            else:
                round_up = False
                output_result = str(digit) + output_result

            i += 1
        return output_result
            



print(Solution().addBinary("100", "110010"))
            