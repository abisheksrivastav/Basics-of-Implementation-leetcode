#You are given the pointer to the head node of a linked list and an integer to add to the list. 
# Create a new node with the given integer. 
# Insert this node at the tail of the linked list and return the head node of the 
# linked list formed after inserting this new node. The given head pointer may be null,
#  meaning that the initial list is empty.

#Function Description

#Complete the insertNodeAtTail function in the editor below.

#insertNodeAtTail has the following parameters:

#SinglyLinkedListNode pointer head: a reference to the head of a list
#int data: the data value for the node to insert
#Returns

#SinglyLinkedListNode pointer: reference to the head of the modified linked list

#SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtTail(head, data):
    if head is None:
        head = SinglyLinkedListNode(data)
        return head
    else:
        temp = head
        while temp.next is not None:
            temp = temp.next
        temp.next = SinglyLinkedListNode(data)
        return head

