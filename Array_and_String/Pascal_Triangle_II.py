class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        else:
            last_row = self.getRow(rowIndex - 1)
            result = [last_row[i] + last_row[i+1] for i in range(len(last_row)-1)] 
            return [1] + result + [1]

print(Solution().getRow(3))