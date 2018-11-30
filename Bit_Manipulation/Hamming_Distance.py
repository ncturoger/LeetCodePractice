class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = self.getBit(x)
        y = self.getBit(y)
        h_dist = 0

        max_cur = max(len(x), len(y))
        cursor = 1
        while cursor <=  max_cur:
            if int(self.getNum(cursor, x)) != int(self.getNum(cursor, y)):
                h_dist += 1
            cursor += 1

        return h_dist

    def getBit(self, x):
        x = int(x)
        result = []
        while(x > 0):
            result.append(x%2)
            x /= 2
        result.reverse()
        return "".join([str(i) for i in result])

    def getNum(self, index, arr):
        if index > len(arr):
            return 0
        else:
            return arr[-index]


print(Solution().hammingDistance(1, 4))

