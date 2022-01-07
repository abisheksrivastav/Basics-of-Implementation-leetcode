#There is a car with capacity empty seats. The vehicle only drives east 
# (i.e., it cannot turn around and drive west).

#You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] 
# indicates that the ith trip has numPassengersi passengers and the locations to pick them up 
# and drop them off are fromi and toi respectively. The locations are given as the number of kilometers 
# due east from the car's initial location.

#Return true if it is possible to pick up and drop off all passengers for all the given trips, 
# or false otherwise.

 

#Example 1:

#Input: trips = [[2,1,5],[3,3,7]], capacity = 4
#Output: false
#Example 2:

#Input: trips = [[2,1,5],[3,3,7]], capacity = 5
#Output: true
 # return boolean if car can pick up and drop off all passengers
        # trips = [[2,1,5],[3,3,7]]
        # capacity = 4
        # return false

class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        # create a dictionary to store the number of passengers per location
        # create a dictionary to store the number of passengers per location
        passengers = {i: 0 for i in range(1001)}
        for trip in trips:
            passengers[trip[1]] += trip[0]
            passengers[trip[2]] -= trip[0]
        # loop through the dictionary and add the passengers
        for i in range(1001):
            capacity -= passengers[i]
            if capacity < 0:
                return False
        return True

# time complexity: O(n)
# space complexity: O(n)

