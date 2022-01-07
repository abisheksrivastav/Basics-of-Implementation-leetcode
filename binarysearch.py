#Given an array of integers nums which is sorted in ascending order, and an integer target,
#  write a function to search target in nums. If target exists,
#  then return its index. Otherwise, return -1.

#You must write an algorithm with O(log n) runtime complexity.
#Example 1:

#Input: nums = [-1,0,3,5,9,12], target = 9
#Output: 4
#Explanation: 9 exists in nums and its index is 4
List = [1,2,3,4,5,6]
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # Binary Search
        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        s = 0 # start
        e = len(nums) - 1 #  end
        while s <= e: # while start is less than or equal to end
            m = (s + e) // 2 # middle
            if nums[m] == target: # if middle is equal to target
                return m # return middle
            elif nums[m] < target: # if middle is less than target
                s = m + 1 # start is middle + 1
            else:
                e = m - 1# end is middle - 1
        return -1


# Time Complexity: O(log n)


