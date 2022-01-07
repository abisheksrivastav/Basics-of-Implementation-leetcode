#Given an array of integers, find the longest subarray where the absolute difference between any 
# two elements is less than or equal to 1 .
#Example
# a = [1,1,2,2,4,4,5,5,5]


#There are two subarrays meeting the criterion:[1,1,2,2] and [4,4,5,5,5] . The maximum length subarray has 
# 5 elements.

#Function Description

#Complete the pickingNumbers function in the editor below.

#pickingNumbers has the following parameter(s):

#int a[n]: an array of integers
#Returns

#int: the length of the longest subarray that meets the criterion

def pickingNumbers(a):
    # Write your code here
    d = {} # dictionary
    for i in a: # for each element in array
        d[i] = d.get(i,0) + 1 # if element is in dictionary, add 1 to value, else add element and value of 1
    max_len = 0 # max length
    for i in d: # for each element in dictionary
        max_len = max(max_len, d[i] + d.get(i+1,0)) # if element + 1 is in dictionary, add value of element + 1 to max length
    return max_len
   


if __name__ == '__main__':
    a = [1 ,2 ,2 ,3 ,1, 2]
    print(pickingNumbers(a))
#a = [1 ,2, 2, 3 ,1, 2]
#print(pickingNumbers(a))
    