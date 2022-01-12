#You are given an m x n binary matrix grid. 
# An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
# You may assume all four edges of the grid are surrounded by water.

#The area of an island is the number of cells with a value 1 in the island.

#Return the maximum area of an island in grid. If there is no island, return 0.

# ex1
#Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
#Output: 6
#Explanation: The answer is not 11, because the island must be connected 4-directionally.
#Example 2:

#Input: grid = [[0,0,0,0,0,0,0,0]]
#Output: 0

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # DFS
        # Time: O(m*n)
        # Space: O(m*n)
        if not grid:
            return 0
        m, n = len(grid), len(grid[0])  # m = number of rows, n = number of columns
        visited = set()                  # create a set to store visited cells
        max_area = 0                      # create a variable to store the maximum area
        for i in range(m):                # O(m)  iterate through each row
            for j in range(n):              # O(n) iterate through each column
                if grid[i][j] == 1 and (i, j) not in visited:   # if the cell is 1 and it has not been visited
                    area = self.dfs(grid, i, j, visited)      # call dfs to find the area of the island
                    max_area = max(max_area, area)       # update the maximum area
        return max_area                           # return the maximum area

    def dfs(self, grid, i, j, visited):  # DFS function
        i = i    # i = row
        j = j      # j = column
        m, n = len(grid), len(grid[0])  # m = number of rows, n = number of columns
        if i < 0 or i >= m or j < 0 or j >= n or (i, j) in visited or grid[i][j] == 0: # if the cell is out of bounds or has been visited or the cell is 0
            return 0   # return 0

        visited.add((i, j)) # add the cell to the visited set
        area = 1      # create a variable to store the area
        area += self.dfs(grid, i + 1, j, visited) # call dfs to find the area of the island
        area += self.dfs(grid, i - 1, j, visited) # call dfs to find the area of the island
        area += self.dfs(grid, i, j + 1, visited)
        area += self.dfs(grid, i, j - 1, visited)
        return area  # return the area





