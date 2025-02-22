# Mr. Vincent works in a door mat manufacturing company. 
# One day, he designed a new door mat with the following specifications:

# Mat size must be NxM. (N is an odd natural number, and M is 3 times N.)
# The design should have 'WELCOME' written in the center.
# The design pattern should only use |, . and - characters.

# ROUGH
n = 11
m = n*3

def print_door_mat(n, m):
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    
    # Print top half
    for line in pattern:
        print(line)
    
    # Print middle line with 'WELCOME'
    print('WELCOME'.center(m, '-'))
    
    # Print bottom half (mirror of top half)
    for line in reversed(pattern):
        print(line)

print_door_mat(n, m)


# SOLUTION
# Enter your code here. Read input from STDIN. Print output to STDOUT
def print_door_mat(n, m):
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    
    # Print top half
    for line in pattern:
        print(line)
    
    # Print middle line with 'WELCOME'
    print('WELCOME'.center(m, '-'))
    
    # Print bottom half (mirror of top half)
    for line in reversed(pattern):
        print(line)

# Input handling
if __name__ == "__main__":
    n, m = map(int, input().split())
    print_door_mat(n, m)