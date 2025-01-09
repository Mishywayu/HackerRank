# We have seen that lists are mutable (they can be changed), and tuples are immutable (they cannot be changed).
# Let's try to understand this with an example.
# You are given an immutable string, and you want to make changes to it.
# Example:
# string = "abracadabra"
# You can access an index by:
# print(string[5]) #output: a
# What if you would like to assign a value?
# string[5] = 'k'

# Task
# Read a given string, change the character at a given index and then print the modified string.

# ROUGH
# Mishelle to Michelle
s = 'Mishelle'
l = list(s)
print(l)
l[2] = 'c'
print(l)
s = str(l) #ooops, didn't work
print(s)

# another way
s = 'Mishy'
l = list(s)
print(l)
l[2] = 'c'
s = ''.join(l)
print(s)