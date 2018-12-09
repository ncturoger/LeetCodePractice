class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        count_list = []
        for item in range(num + 1):
            count_list.append(self.countBitOnes(item))

        return count_list
    

    def countBitOnes(self, number):
        count = 0
        while number > 0:
            if number % 2 == 1:
                count += 1
            number = int(number / 2)
        
        return count



assert Solution().countBits(2) == [0,1,1]
assert Solution().countBits(5) == [0,1,1,2,1,2]