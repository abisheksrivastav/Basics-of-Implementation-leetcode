#An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

#You are also given three integers sr, sc, and newColor. 
# You should perform a flood fill on the image starting from the pixel image[sr][sc].

#To perform a flood fill, consider the starting pixel, 
# plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, 
# plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. 
# Replace the color of all of the aforementioned pixels with newColor.

#Return the modified image after performing the flood fill.

 

#Example 1:


#Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
#Output: [[2,2,2],[2,2,0],[2,0,1]]
#Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
# all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) 
# are colored with the new color.
#Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
#Example 2:

#Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
#Output: [[2,2,2],[2,2,2]]

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def dfs(i, j, color
        ):                       # i, j is the position of the pixel
            if i < 0 or i >= len(image) or j < 0 or j >= len(image[0]):  # out of bound
                return   # return if out of bound
            if image[i][j] != color:   # if the pixel is not the same color as the starting pixel
                return       # return if not the same color
            image[i][j] = newColor   # change the color of the pixel
            dfs(i + 1, j, color) # go to the right
            dfs(i - 1, j, color) # go to the left
            dfs(i, j + 1, color) # go to the bottom
            dfs(i, j - 1, color) # go to the top

        color = image[sr][sc]    # get the color of the starting pixel
        if color == newColor:    # if the starting pixel is the same color as the new color
            return image       # return the image
        dfs(sr, sc, color)  # start the dfs
        return image       # return the image
