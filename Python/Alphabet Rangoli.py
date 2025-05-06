# You are given an integer, N.
# Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)

# ROUGH WORK
# def alphabet_rangoli (size):
#     import string
#     letters = string.ascii_lowercase

#     pattern = []

#     # The top half
#     for i in range(size):
#         left = letters[size-1:i:-1] #left side - from current letter down to letter 'a'
#         right = letters[i:size] #right side - from current letter to end letter
#         row = "-".join(left + right) #combine both sides
#         row = row.center(4*size - 3, "-") #center the row using dashes to align properly

#         pattern.append(row)

#     #The bottom half - mirror the top half to get the full rangoli
#     for row in reversed(pattern[:-1]):
#         pattern.append(row)

#     #print each line
#     for row in pattern:
#         print(row)

# alphabet_rangoli(10)

# ----The output is not the correct one

def print_rangoli(size):
    import string
    letters = string.ascii_lowercase
    pattern = []

    for i in range(size):
        # Create the left and right sides of the row
        left = letters[size-1:i:-1]
        right = letters[i:size]
        row = '-'.join(left + right)
        # Center the row to make symmetrical pattern
        row = row.center(4*size - 3, '-')
        pattern.append(row)

    # Mirror the top half to create the full rangoli
    full_rangoli = pattern[::-1] + pattern[1:]

    # Print each line
    for row in full_rangoli:
        print(row)

print_rangoli(5)


# solution
def print_rangoli(size):
    # your code goes here
    import string
    letters = string.ascii_lowercase
    
    pattern = []
    
    for i in range(size):
        left = letters[size-1:i:-1]
        right = letters[i:size]
        row = "-".join(left + right)
        
        row = row.center(4*size - 3, "-")
        pattern.append(row)
        
    full_rangoli = pattern[::-1] + pattern[1:]
        
    for row in full_rangoli:
        print(row)

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)