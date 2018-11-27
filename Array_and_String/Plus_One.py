class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digit = digits[-1] + 1
        if digit != 10:
            digits[-1] = digit
        
        else:
            for i in range(1,len(digits) + 1):
                digit = digits[-i] + 1
                if digit == 10:
                    digits[-i] = 0
                    if i == len(digits):
                        digits.insert(0, 1)
                
                else:
                    digits[-i] = digit
                    break

        return digits
        
            