#You are given an unordered array consisting of consecutive integers belongs [1, 2, 3, ..., n] 
# without any duplicates. You are allowed to swap any two elements. 
# Find the minimum number of swaps required to sort the array in ascending order.
#Sample Input 0

#4
#4 3 1 2
#Sample Output 0
#3
#Explanation 0
#Given array  arr = [4, 3, 1, 2]
#After swapping(0,2)  we get arr = [1, 3, 4, 2]
#After swapping (1,2) we get arr = [1,4,3,2]
#After swapping(1,3)  we get arr = [1,2,3,4]
#So, we need a minimum of  3 swaps to sort the array in ascending order.

def minimumSwaps(arr):
   s = {} # s[i] = index of i-th element
   for i in range(len(arr)):#i=0,1,2,3
      s[arr[i]] = i # s[4] = 0, s[3] = 1, s[2] = 2, s[1] = 3
   count = 0 # number of swaps
   for i in range(len(arr)):
      if arr[i] != i+1: # if arr[i] != i+1
         j = s[i+1] # j = index of i+1-th element
         arr[i], arr[j] = arr[j], arr[i] # swap i-th and j-th elements
         s[arr[i]] = i # update s[4] = 0, s[3] = 1, s[2] = 2, s[1] = 3
         s[arr[j]] = j # update s[4] = 0, s[3] = 1, s[2] = 2, s[1] = 3
         count += 1 # increment count
   return count
    