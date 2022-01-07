#Given the head of a singly linked list, return true if it is a palindrome.
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        if head is None:
            return True
        else:
            x_str = ''
            x_list = []
            while head is not None:
                x_list.append(head.val)
                head = head.next
            x_len = len(x_list)
            for i in range(x_len):
                x_str = x_str + str(x_list[i])
            return x_str == x_str[::-1]
       
            