# what is brute force?
# brute force is a method of solving a problem by trying every possible combination of values.


# brute force
# brute force algorithm

def brute_force(n):#n is the number of digits
    for i in range(1, n+1):# i is the first number
        for j in range(1, n+1):# j is the second number
            for k in range(1, n+1):# k is the third number
                if i + j + k == n:# if the sum of i, j, k is equal to n
                    print(i, j, k) # print the numbers

