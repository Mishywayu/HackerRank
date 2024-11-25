# Task
# The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:

# The first line contains the sum of the two numbers.
# The second line contains the difference of the two numbers (first - second).
# The third line contains the product of the two numbers.

# ROUGH
a = 10
b = 30

print(a + b)
print (a - b)
print (a * b)

# SOLUTION
if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
    print(a + b)
    print (a - b)
    print (a * b)