#Given a string s, reverse the order of characters in each word 
# within a sentence while still preserving whitespace and initial word order.
#Example 1:

#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"
#Example 2:

#Input: s = "God Ding"
#Output: "doG gniD"

class Solution:
    def reverseWords(self, s: str) -> str:

        # two pointer and in a recursive way
        # s = "Let's take LeetCode contest"

        d = s.split()  # ['Let', 's', 'take', 'LeetCode', 'contest']
        res = []      # []
        for i in d:    # ['Let', 's', 'take', 'LeetCode', 'contest']
            res.append(i[::-1])  
        return ' '.join(res)   # 's'teL ekat edoCteeL tsetnoc'




  

       
    
    

 

if __name__ == '__main__':
        s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))