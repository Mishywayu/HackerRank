# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# NOTE: String letters are case-sensitive.
# Sample input:
# ABCDCDC
# CDC
# Output:
# 2

# ROUGH
main = 'ABCDCDC'
sub = 'CDC'

def find():
    count = 0
    start = 0
    
    while start < len(main):
        start = main.find(sub, start)
        if start == -1:
            break
        count = count + 1
        start = start + 1
    return count

print(find())