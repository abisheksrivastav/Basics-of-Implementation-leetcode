#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
# find two numbers such that they add up to a specific target number. 
# Let these two numbers be numbers[index1] and numbers[index2] 
# where 1 <= index1 < index2 <= numbers.length.

#Return the indices of the two numbers, index1 and index2, 
# added by one as an integer array [index1, index2] of length 2.

#The tests are generated such that there is exactly one solution. You may not use the same element twice.
#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

List = [1,2,3,4,5,6]
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
      # why we take empty dictionary?
        # because we need to return the index of the pair
        # so we need to store the index of the pair
        # target - value is the key
        # i is the value
        

        
        s = {} # Empty dictionary
        for i, value in enumerate(numbers):# enumerate is a function that returns a tuple containing a counter (the index) and the value of the list at that index
            if target - value in s:# if target - value is in s, then we have found a pair
                return [s[target - value] + 1, i + 1] # return the index of the pair
            s[value] = i # add the value to the dictionary


