# This is an to practice traversing a linked list. 
# Given a pointer to the head node of a linked list, print each node's data element, one per line.
#  If the head pointer is null (indicating the list is empty), there is nothing to print.

#Function Description

#Complete the printLinkedList function in the editor below.

#printLinkedList has the following parameter(s):

#SinglyLinkedListNode head: a reference to the head of the list
#Print

#For each node, print its   data value on a new line

def printLinkedList(head):
    while head:
        print(head.data)
        head = head.next
        
