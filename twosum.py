#Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.

#You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.

#You can return the answer in any order.
# brute force algorithm
# def twoSum(nums, target):
#     """
#     :type nums: List[int]
#     :type target: int
#     :rtype: List[int]
#     """
#     for i in range(len(nums)):




List = [2, 7, 11, 15]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:  # O(n)
         s = {} # O(1)# Empty dictionary
         for i, value in enumerate(nums): # O(n) # enumerate is a function that returns a tuple containing a counter (the index) and the value of the list at that index
                if target - value in s: # O(1) # if target - value is in s, then we have found a pair
                    return [s[target - value], i]# O(1) # return the index of the pair
                s[value] = i # O(1) # add the value to the dictionary

        
  



 