#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        else:
            x_str = str(x)
            x_len = len(x_str)
            for i in range(x_len):
                if x_str[i] != x_str[x_len - 1 - i]:
                    return False
            return True