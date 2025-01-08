# # In Python, a string can be split on a delimiter.
# Example:
# a = "this is a string"
# a = a.split(" ") # a is converted to a list of strings. 
# print a
# ['this', 'is', 'a', 'string']

# Joining a string is simple:
# Example:
# a = "-".join(a)
# print a
# this-is-a-string 

# Task
# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

# ROUGH
name = "This is upskilling in Python"
# splitting
a = name.split(" ")
print(f"This is spilliting variable 'name': Output: {a}") #Output: ['This', 'is', 'upskilling', 'in', 'Python']
# joining
b = "-".join(a)
print(f"This is joining variable 'a': Output: {b} ") #Output: This-is-upskilling-in-Python


# SOLUTION
def split_and_join(line):
    # write your code here
    line = line.split(" ")
    line = "-".join(line)
    return line
    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)