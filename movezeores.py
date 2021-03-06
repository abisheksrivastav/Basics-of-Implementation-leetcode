#Given an integer array nums, move all 0's to the end of it while maintaining the 
# relative order of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

 

#Example 1:

#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
#Example 2:

#Input: nums = [0]
#Output: [0]

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        for i in range(len(nums)): # i=0,1,2,3
            if nums[i] == 0: # if nums[i] == 0
                nums.remove(nums[i]) # remove nums[i]
                nums.append(0) # append 0
