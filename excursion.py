#A group of students wants to visit a tour in some city X . 
# In total, the group has N boys and M girls. To do this, they need to stay in a hotel.

#Calculate the number of rooms you need to book in the hotel, 
# if each hotel room has K seats, provided that the boys can not live with the girls in the same room.

#Input format

#The first line specifies a number T denoting the number of test cases.
#In each line of the test case, there are three numbers,N,M,K .
#Output format

#For each test case, print one number denoting the number of rooms to be booked at the hotel.
# eg 
# Input:
#4
#13 7 2
#5 5 3
# output :
#11
#4
#Explanation:
#For test 13 7 2 answer is 11, because need for boys 7 rooms and for girls need 4 room
#For test 5 5 3 answer is 4, because need for boys 2 rooms and for girls need 2 rooms


# room occupied by boys and girls

for _ in range(int(input())): # 
    
    [n,m,k]=list(map(int,input().split())) 

    total=0

    while n>0:

        total+=1

        n-=k

    while m>0:

        total+=1

        m-=k

    print(total)




    
          

        
 







    

    

       
   
    