#Given the head of a singly linked list, return the middle node of the linked list.

#If there are two middle nodes, return the second middle node.
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]
#Explanation: The middle node of the list is node 3.
#Example 2:


#Input: head = [1,2,3,4,5,6]
#Output: [4,5,6]
#Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # input 
        # head = [1,2,3,4,5]
        # output = [3,4,5]
        # middle node = 3
        # example 2:
        # input = [1,2,3,4,5,6]
        # output = [4,5,6]
        # middle node = 4

        # edge case
         if head == None:   # if head is None
             return None
         if head.next == None:    # if head.next is None

             return head          # return head
         if head.next.next == None:  # if head.next.next is None
            return head.next          # return head.next

        # initialize
         current = head      # current = head
         middle = head        # middle = head
         count = 0
         while current != None:  # while current is not None
            current = current.next  # current = current.next
            count += 1               # count += 1
            if count % 2 == 0:       # if count % 2 == 0
                middle = middle.next   # middle = middle.next
         return middle


