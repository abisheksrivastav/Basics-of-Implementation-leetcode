
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # print_list 
    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next



# append node to the end of the linked list

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
# insert after node 
    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node is not in the list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node
# delete node
    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node = None
            return
        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next
        if curr_node is None:
            return
        prev.next = curr_node.next
        curr_node = None


# delete node at pos 
    def delete_node_at_pos(self, pos):
        if self.head:
            curr_node = self.head
            if pos == 0:
                curr_node = curr_node.next
                self.head = curr_node
                return
            prev = None
            count = 0
            while curr_node and count != pos:
                prev = curr_node
                curr_node = curr_node.next
                count += 1
            if curr_node is None:
                return
            prev.next = curr_node.next
            curr_node = None

    # node swapping
    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return
        prev_1 = None
        curr_1 = self.head
        while curr_1 and curr_1.data != key_1:
            prev_1 = curr_1
            curr_1 = curr_1.next
        prev_2 = None
        curr_2 = self.head
        while curr_2 and curr_2.data != key_2:
            prev_2 = None
            curr_2 = curr_2.next
        if not curr_1 or not curr_2:
            return
        if prev_1:
            prev_1.next = curr_2
        else:
            self.head = curr_2
        if prev_2:
            prev_2.next = curr_1
        else:
            self.head = curr_1
        curr_1.next, curr_2.next = curr_2.next, curr_1.next

        # Merge two sorted linked lists
    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            q = self.head
            return q
        if not q:
            p = self.head
            return p
        if p and q:
            p = self.head
            q = llist.head
            if p.data <= q.data:
                p = p.next
                s = p
            else:
                q = q.next
                s = q
        while p and q:
            if p.data <= q.data:
                p = p.next
                s.next = p
            else:
                q = q.next
                s.next = q
            s = s.next
        if not p:
            s.next = q
        if not q:
            s.next = p
        return self.head
        

# to remove duplicates from the linked list
    def remove_duplicates(self):
        curr = self.head
        prev = None
        dup_values = dict()
        while curr:
            if curr.data in dup_values:
                prev.next = curr.next
            else:
                dup_values[curr.data] = 1
                prev = curr
            curr = curr.next
        return self.head

        # to count the number of nodes in the linked list
    def count_nodes(self):
        curr = self.head
        count = 0
        while curr:
            count += 1
            curr = curr.next
        return count

        # to find the middle of the linked list
    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head
        if self.head is not None:
            while (fast_ptr is not None and fast_ptr.next is not None):
                fast_ptr = fast_ptr.next.next
                slow_ptr = slow_ptr.next
        return slow_ptr

        # to find the nth node from the end of the linked list
    def find_nth_from_end(self, n):
        temp = self.head
        size = 0
        while temp:
            size += 1
            temp = temp.next
        temp = self.head
        for i in range(size-n):
            temp = temp.next
        return temp

        # to find the intersection of two linked lists
    def find_intersection(self, llist):
        p = self.head
        q = llist.head
        if p is None or q is None:
            return
        while p is not q:
            if p is not None:
                p = p.next
            if q is not None:
                q = q.next
        return p

        # move last node to the beginning
    def move_last_to_front(self):
        temp = self.head   # store head
        while temp.next is not None:   # find the last node
            prev = temp               # store the previous node
            temp = temp.next           # move to the next node
        prev.next = None               # break the link with the last node
        temp.next = self.head          # move the last node to the beginning
        self.head = temp                # update the head

        # sum of two linked lists
    def add_two_numbers(self, llist):
        p = self.head
        q = llist.head
        carry = 0
        while p or q:
            if p:
                carry += p.data
                p = p.next
            if q:
                carry += q.data
                q = q.next
        if carry > 9:
            carry = carry % 10
            temp = Node(carry)
            temp.next = self.head
            self.head = temp
        return self.head

        # reverse a linked list

        


   
      

        


















if __name__ == '__main__':
    llist_1 = LinkedList()
    llist_2 = LinkedList()

llist_1.append(1)
llist_1.append(5)
llist_1.append(7)
llist_1.append(9)
llist_1.append(10)

llist_2.append(2)
llist_2.append(3)

llist_2.append(4)
llist_2.append(6)
llist_2.append(8)

llist_1.merge_sorted(llist_2)
llist_1.print_list()





                