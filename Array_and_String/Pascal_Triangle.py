class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        if numRows == 1:
            return [[1]]
        
        elif numRows == 2:
            return [[1], [1, 1]]

        else:
            result_row = [[1], [1, 1]]
            last_row = [1, 1]
            for row in range(3, numRows + 1):
                layer_row = [1]
                for i in range(len(last_row) - 1):
                    layer_row.append(last_row[i] + last_row[i+1])
                layer_row.append(1)
                result_row.append(layer_row)
                last_row = layer_row
            
            return result_row
                
print(Solution().generate(5))