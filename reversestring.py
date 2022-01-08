#Write a function that reverses a string. The input string is given as an array of characters s.

#You must do this by modifying the input array in-place with O(1) extra memory.

 

#Example 1:

#Input: s = ["h","e","l","l","o"]
#Output: ["o","l","l","e","h"]
#Example 2:

#Input: s = ["H","a","n","n","a","h"]
#Output: ["h","a","n","n","a","H"]


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        
        s1 = len(s)
        s2 = s1//2
        for i in range(s2):
                s[i],s[s1-i-1] = s[s1-i-1],s[i]
        return s
 

# Time Complexity: O(n)
# Space Complexity: O(1)
# two pinters to swap the values
# two pointers to move through the list


 

 
          
          