#The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
# (you may want to display this pattern in a fixed font for better legibility)

#P   A   H   N
#A P L S I I G
#Y   I   R
#And then read line by line: "PAHNAPLSIIGYIR"

#Write the code that will take a string and make this conversion given a number of rows:

#string convert(string s, int numRows);
 

#Example 1:

#Input: s = "PAYPALISHIRING", numRows = 3
#Output: "PAHNAPLSIIGYIR"
#Example 2:

#Input: s = "PAYPALISHIRING", numRows = 4
#Output: "PINALSIGYAHRPI"
#Explanation:
#P     I    N
#A   L S  I G
#Y A   H R
#P     I
#Example 3:

#Input: s = "A", numRows = 1
#Output: "A"

class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1:  # if numRows is 1, return the original string
            return s
        result = [''] * numRows  # initialize the result list
        index, step = 0, 1            # initialize the index and step
        for x in s:                    # for each character in the string
            result[index] += x          # add the character to the result list
            if index == 0:           # if index is 0

                step = 1               # step is 1
            elif index == numRows - 1:  # if index is numRows - 1
                step = -1               # step is -1
            index += step               # increment index by step
        return ''.join(result)          # return the result list joined into a string