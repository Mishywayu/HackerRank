# TASK
# Given an integer, n, print the following values for each integer i from n to :
# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# ROUGH
n = 5

for i in range(1, n+1):
    print(f"In Decimal is: {i:d}")
    print(f"In Octal is: {i:o}")
    print(f"In Hexadecimal is: {i:X}")
    print(f"In Binary is: {i:b}")
    print()

# SOLUTION
def print_formatted(number):
    # your code goes here
    width = len(bin(n)) - 2  # Calculate the width for formatting
    for i in range(1, n+1):
        print(f"{i:{width}d} {i:{width}o} {i:{width}X} {i:{width}b}")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)