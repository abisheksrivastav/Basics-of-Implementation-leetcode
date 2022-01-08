#Given a binary array nums, return the maximum number of consecutive 1's in the array.

#Example 1:

#Input: nums = [1,1,0,1,1,1]
#Output: 3
#Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
#Example 2:

#Input: nums = [1,0,1,1,0,1]
#Output: 2

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        for i in range(len(nums)):        # iterate through the array
            if nums[i] == 0:              # if the element is 0
                nums[i] = -1               # change it to -1
        nums.append(-1)                    # append -1 to the end of the array
        max_count = 0                      # initialize max_count to 0
        count = 0                          # initialize count to 0
        for i in range(len(nums)):         # iterate through the array
            if nums[i] == 1:              # if the element is 1
                count += 1                  # increment count by 1
            else:
                if count > max_count:        # if count is greater than max_count
                    max_count = count         # update max_count to count
                count = 0                      # reset count to 0
        return max_count