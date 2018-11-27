class Solution_1(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        start_positions = []
        traverse_path = []

        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for col in range(cols):
                start_positions.append((0, col))
            
            for row in range(1, rows):
                start_positions.append((row, cols-1))

            need_reverse = False
            print(start_positions)
            for idx, start_position in enumerate(start_positions):
                row, col = start_position
                need_reverse = idx % 2 == 0
                path = []
                while(col > -1 and row < rows):
                    path.append(matrix[row][col])
                    row += 1
                    col -= 1
                
                if need_reverse:
                    path.reverse()
                
                traverse_path += path
        
        return traverse_path


class Solution_2(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        start_positions = []
        traverse_path = []

        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            for col in range(cols):
                start_positions.append((0, col))
            
            for row in range(1, rows):
                start_positions.append((row, cols-1))

            need_reverse = False
            print(start_positions)
            for idx, start_position in enumerate(start_positions):
                row, col = start_position
                need_reverse = idx % 2 == 0
                path = []
                while(col > -1 and row < rows):
                    if need_reverse:
                        path.insert(0, matrix[row][col])
                    else:
                        path.append(matrix[row][col])
                    row += 1
                    col -= 1
                
                traverse_path += path
        
        return traverse_path


print(Solution().findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]))
        