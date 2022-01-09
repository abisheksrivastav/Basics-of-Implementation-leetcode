#Convert Decimal Integer to Binary

#In this coding exercise, you are required to use the stack data structure to convert 
# integer values to their binary equivalent.

#Division by 2 Method

from stack import Stack

def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        rem = dec_num % 2
        s.push(rem)
        dec_num = dec_num // 2
    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())
    return bin_num