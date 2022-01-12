#Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

#In other words, return true if one of s1's permutations is the substring of s2.

 

#Example 1:

#Input: s1 = "ab", s2 = "eidbaooo"
#Output: true
#Explanation: s2 contains one permutation of s1 ("ba").
#Example 2:

#Input: s1 = "ab", s2 = "eidboaoo"
#Output: false

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Hash table  O(n)
         if len(s1) > len(s2):  # if s1 is longer than s2, return false
                return False
         s1_hash = {}         # create a hash table for s1
         for i in s1:            # O(n)
            if i in s1_hash:   # if the character is in the hash table, add 1 to its value
                s1_hash[i] += 1
            else:
                s1_hash[i] = 1    # if the character is not in the hash table, add it to the hash table and set its value to 1
         s2_hash = {}             # create a hash table for s2
         for i in s2[:len(s1)]:      # O(n) 
            if i in s2_hash:          # if the character is in the hash table, add 1 to its value
                s2_hash[i] += 1
            else:
                s2_hash[i] = 1       # if the character is not in the hash table, add it to the hash table and set its value to 1
         if s1_hash == s2_hash:
            return True
         for i in range(len(s2) - len(s1)):  # O(n)
            if s2[i] in s2_hash:             
                s2_hash[s2[i]] -= 1      # if the character is in the hash table, subtract 1 from its value
                if s2_hash[s2[i]] == 0:     # if the value of the character in the hash table is 0, remove it from the hash table
                    del s2_hash[s2[i]] # if the value of the character in the hash table is 0, delete it
            if s2[i + len(s1)] in s2_hash:  # if the character is in the hash table, add 1 to its value
                s2_hash[s2[i + len(s1)]] += 1
            else:
                s2_hash[s2[i + len(s1)]] = 1
            if s1_hash == s2_hash:
                return True
         return False

         
      