#You are a product manager and currently leading a team to develop a new product. Unfortunately,
# the latest version of your product fails the quality check. 
# Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad.

#Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, 
# which causes all the following ones to be bad.

#You are given an API bool isBadVersion(version) which returns whether version is bad. 
# Implement a function to find the first bad version. You should minimize the number of calls to the API.

#Input: n = 5, bad = 4
#Output: 4
#Explanation:
#call isBadVersion(3) -> false
#call isBadVersion(5) -> true
#call isBadVersion(4) -> true
#Then 4 is the first bad version

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = 1# start
        e = n # end
        while s < e:# while start is less than end
            mid = s + (e - s) // 2 # midpoint
            if isBadVersion(mid):# if midpoint is bad
                e = mid # end is midpoint
            else:
                s = mid + 1# start is midpoint + 1
        return s # return start


