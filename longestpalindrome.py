#Given a string s, return the longest palindromic substring in s.
#Example 1:

#Input: s = "babad"
#Output: "bab"
#Explanation: "aba" is also a valid answer
#Example 2:
#Input: s = "cbbd"
#Output: "bb"
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if len(s) == 0:
            return ''
        elif len(s) == 1:
            return s
        elif len(set(s))==1:
            return s
        else:
            result = ''
            lp = 0
            rp = 0
            for i in range(len(s)-1):
                if s[i]==s[i+1]:
                    lp = i
                    rp = i+1
                    while lp>0 and rp<len(s)-1:
                        if s[lp-1] == s[rp+1]:
                            lp-=1
                            rp+=1
                        else:
                            break
                    st = s[lp:rp+1]
                    if len(st)>len(result):
                        result = st
                if i>0 and s[i-1]==s[i+1]:
                    lp = i-1
                    rp = i+1
                    while lp>0 and rp<len(s)-1:
                            if s[lp-1] == s[rp+1]:
                                lp-=1
                                rp+=1
                            else:
                                break
                    st = s[lp:rp+1]
                    if len(st)>len(result):
                        result = st
            return s[0] if result == "" else result
   






       
        
    



    
 





        