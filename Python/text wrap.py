# You are given a string S and w width .
# Your task is to wrap the string into a paragraph of width w.

# Function Description
# Complete the wrap function in the editor below.
# wrap has the following parameters:
# 1. string string: a long string
# 2. int max_width: the width to wrap to

# ROUGH
import textwrap

string = 'Michelle'
max_width = 2

print(textwrap.wrap(string,max_width))


# SOLUTION
import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string, max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)