# Task
# The provided code stub reads and integer, n, from STDIN. 
# For all non-negative integers i < n, print square of i.

# Example
# n = 3
# The list of non-negative integers that are less than n = 3 is [0,1,2]. 
# Print the square of each number on a separate line.
# 0
# 1
# 4

# ROUGH
n = 3

for i in range(n):
    print(i**2)

# SOLUTION
if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        print(i**2)