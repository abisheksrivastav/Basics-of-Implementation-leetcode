# Given a string s and an integer k, 
# reverse the first k characters for every 2k characters counting from the start of the string.

#If there are fewer than k characters left, reverse all of them. 
# If there are less than 2k but greater than or equal to k characters, then reverse the first k 
# characters and left the other as original.

 

#Example 1:

#Input: s = "abcdefg", k = 2
#Output: "bacdfeg"
#Example 2:

#Input: s = "abcd", k = 2
#Output: "bacd"

class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        # s = "abcdefg" , k = 2
        # output = "bacdfeg"

        # s = "abcd" , k = 2
        # output = "bacd"

        
        s = list(s)  # ['a', 'b', 'c', 'd', 'e', 'f', 'g']
        for i in range(0, len(s), 2*k):  # 0, 2, 4, 6
            s[i:i+k] = s[i:i+k][::-1]  # [::-1] reverse the list
        return ''.join(s)


if __name__ == '__main__':
    s = "abcdefg"
    k = 2
    print(Solution().reverseStr(s, k))



         

      

