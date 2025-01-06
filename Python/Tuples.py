# Given an integer, n, and n space-separated integers as input, create a tuple, t, 
# of those n integers. Then compute and print the result of hast(t).

# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

# Input Format
# The first line contains an integer, n, denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.

# Output Format
# input: 2
#        12
# output: 3713081631934410656

# ROUGH
tuple = ('apple', 'banana', 'cherry')
result = hash(tuple)
print(result)
# output: 2977451544500717804, possible to has a tuple


# SOLUTION
n = int(input())
integer_list = tuple(map(int, input().split()))
result = hash(integer_list)
print(result)