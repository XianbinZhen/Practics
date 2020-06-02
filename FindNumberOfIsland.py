# Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks),
# count the number of islands present in the grid. The definition of an island is as follows:
# 1.) Must be surrounded by water blocks.
# 2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
# Assume all edges outside of the grid are water.
# Example:
# Input:
# 10001
# 11000
# 10110
# 00000
# Output: 3
# Here's your starting point:
# class Solution(object):
#   def inRange(self, grid, r, c):
#     numRow, numCol = len(grid), len(grid[0])
#     if r < 0 or c < 0 or r >= numRow or c >= numCol:
#       return False
#     return True
#   def numIslands(self, grid):
#     # Fill this in.
# grid = [[1, 1, 0, 0, 0],
#         [0, 1, 0, 0, 1],
#         [1, 0, 0, 1, 1],
#         [0, 0, 0, 0, 0]]
# print(Solution().numIslands(grid))
# # 3

class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        row = len(grid)
        colum = len(grid[0])
        more = True
        while more:
            more = False
            for i in range(row):
                for j in range(colum):
                    if grid[i][j] == 1:
                        neighbor_count = 0
                        # print("grid at: ", i, j)
                        left = j - 1
                        right = j + 1
                        up = i - 1
                        down = i + 1
                        if left >= 0:
                            # print("left neighbor: ", grid[i][left])
                            neighbor_count += grid[i][left]
                        if right < colum:
                            # print("right neighbor: ", grid[i][right])
                            neighbor_count += grid[i][right]
                        if up >= 0:
                            # print("up neighbor: ", grid[up][j])
                            neighbor_count += grid[up][j]
                        if down < row:
                            # print("down neighbor: ", grid[down][j])
                            neighbor_count += grid[down][j]
                        if neighbor_count == 1:
                            # print("neighbor count: ", neighbor_count)
                            grid[i][j] = 0
                            # print("remove i j:", i, j)
                            # print(grid)
                            more = True
        more = True
        while more:
            more = False
            for i in range(row):
                for j in range(colum):
                    if grid[i][j] == 1:
                        neighbor_count = 0
                        print("grid at: ", i, j)
                        left = j - 1
                        right = j + 1
                        up = i - 1
                        down = i + 1
                        if left >= 0:
                            # print("left neighbor: ", grid[i][left])
                            neighbor_count += grid[i][left]
                        if right < colum:
                            # print("right neighbor: ", grid[i][right])
                            neighbor_count += grid[i][right]
                        if up >= 0:
                            # print("up neighbor: ", grid[up][j])
                            neighbor_count += grid[up][j]
                        if down < row:
                            # print("down neighbor: ", grid[down][j])
                            neighbor_count += grid[down][j]
                        if neighbor_count == 1 or neighbor_count == 2:
                            print("neighbor count: ", neighbor_count)
                            grid[i][j] = 0
                            print("remove i j:", i, j)
                            # print(grid)
                            more = True
        result = 0
        for i in range(row):
            for j in range(colum):
                if grid[i][j] == 1:
                    result += 1
        return result


grid = [[1, 1, 1, 0, 1],
        [0, 1, 0, 1, 1],
        [1, 0, 0, 1, 1],
        [0, 1, 1, 1, 1]]
print(Solution().numIslands(grid))
