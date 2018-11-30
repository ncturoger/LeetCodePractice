class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if grid:
            self.max_row = len(grid)
            self.max_col = len(grid[0])
            self.checked_position = [[False for i in range(self.max_col)] for j in range(self.max_row)]
            self.grid = grid

            island_count = 0

            for i in range(self.max_row):
                for j in range(self.max_col):
                    if not self.checked_position[i][j]:
                        if grid[i][j] == "1":
                            island_count += 1
                            self.check_adjacent(i, j)
        
            return island_count
        
        else:
            return 0

    def check_adjacent(self, row, col):
        self.checked_position[row][col] = True
        if row > 0:
            if self.grid[row - 1][col] == "1":
                if not self.checked_position[row - 1][col]:
                    self.check_adjacent(row-1, col)

        if col > 0:
            if self.grid[row][col - 1] == "1":
                if not self.checked_position[row][col - 1]:
                    self.check_adjacent(row, col - 1)

        if row < self.max_row - 1:
            if self.grid[row + 1][col] == "1":
                if not self.checked_position[row + 1][col]:
                    self.check_adjacent(row+1, col)

        if col < self.max_col - 1:
            if self.grid[row][col + 1] == "1":
                if not self.checked_position[row][col + 1]:
                    self.check_adjacent(row, col + 1)

print(Solution().numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))

