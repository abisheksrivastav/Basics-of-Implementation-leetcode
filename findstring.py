# find the string  in substring using find method

def findstring(string, substring):
    if string.find(substring) != -1:
        print("String found")
    else:
        print("String not found")

string = input("Enter the string: ")
substring = input("Enter the substring: ")
findstring(string, substring)