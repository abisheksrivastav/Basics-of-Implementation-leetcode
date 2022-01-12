# ex1 
# arr = [0,1,2,1,2,3]
# the largest such array has length 4
# [1,2,1,2]

# ex2 
# arr = [1,1,1,3,3,2,2]
# the largest such array has length 4
# [3,3,2,2]
# the value 1 and 3 differ by more than  1 so [1,1,1,3,3] is not valid
#Given an array  of integers , what is the length  of th the longest subarray containing no more than two distinct values such that 
# the distinct value differ by no more that 1

def longestSubarray(arr):
    ##Given an array  of integers , what is the length  of th the longest subarray containing no more than two distinct values such that 
# the distinct value differ by no more that 1
 # arr2 = [1,2,3,4,5]
 # output : 2
 # explanation all the elements are distinct,so any subaray of length 2 is maximum
    # arr3 = [1,2,3,4,5,6]
    # output : 3
    # explanation all the elements are distinct,so any subaray of length 3 is maximum
    s ={}
    max_length = 0
    start = 0
    end = 0
    for i in range(len(arr)):
        if arr[i] not in s:
            s[arr[i]] = 1
            end += 1
            max_length = max(max_length, end - start)
        else:
            s[arr[i]] += 1
            end += 1
            max_length = max(max_length, end - start)
            while s[arr[start]] > 1:
                s[arr[start]] -= 1
                start += 1
                max_length = max(max_length, end - start)
    return max_length








     

   
  





