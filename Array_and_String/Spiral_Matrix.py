class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        direction = 1
        path = []

        if matrix:
            rows = len(matrix)
            cols = len(matrix[0])
            total_element = rows * cols
            traverse_count = 0

            row = col = 0
            while traverse_count < total_element:
                if direction == 1:
                    if col < cols:
                        if col == cols - 1 or matrix[row][col+1] in path:
                            if traverse_count + 1 == total_element:
                                path.append(matrix[row][col])
                                traverse_count += 1

                            direction = self.next_direction(direction)

                        else:
                            path.append(matrix[row][col])
                            traverse_count += 1
                            col += 1

                elif direction == 2:
                    if row < rows:
                        if row == rows - 1 or matrix[row+1][col] in path:
                            if traverse_count + 1 == total_element:
                                path.append(matrix[row][col])
                                traverse_count += 1

                            direction = self.next_direction(direction)

                        else:
                            path.append(matrix[row][col])
                            traverse_count += 1
                            row += 1

                elif direction == 3:
                    if col > -1:
                        if col == 0 or matrix[row][col-1] in path:
                            if traverse_count + 1 == total_element:
                                path.append(matrix[row][col])
                                traverse_count += 1

                            direction = self.next_direction(direction)

                        else:
                            path.append(matrix[row][col])
                            traverse_count += 1
                            col -= 1

                elif direction == 4:
                    if row > -1:
                        if row == 0 or matrix[row-1][col] in path:
                            if traverse_count + 1 == total_element:
                                path.append(matrix[row][col])
                                traverse_count += 1

                            direction = self.next_direction(direction)

                        else:
                            path.append(matrix[row][col])
                            traverse_count += 1
                            row -= 1

        return path


    def next_direction(self, direction):
        next_direct = direction + 1 if direction != 4 else 1
        return next_direct

print(Solution().spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]]))