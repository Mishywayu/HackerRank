# Python has built-in string validation methods for basic data. It can check if a string is composed of 
# alphabetical characters, alphanumeric characters, digits, etc.

# str.isalnum() -This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9).
# str.isalpha() -This method checks if all the characters of a string are alphabetical (a-z and A-Z).
# str.isdigit() -This method checks if all the characters of a string are digits (0-9).
# str.islower() -This method checks if all the characters of a string are lowercase characters (a-z).
# str.isupper() -This method checks if all the characters of a string are uppercase characters (A-Z).

# TASK
# You are given a string s.
# Your task is to find out if the string s contains: alphanumeric characters, alphabetical characters, digits, 
# lowercase and uppercase characters.

# Output Format
# In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if s has any alphabetical characters. Otherwise, print False.
# In the third line, print True if s has any digits. Otherwise, print False.
# In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if s has any uppercase characters. Otherwise, print False.


#ROUGH
string = 'qA2'

print(any(char.isalnum() for char in string))  
print(any(char.isalpha() for char in string))  
print(any(char.isdigit() for char in string))  
print(any(char.islower() for char in string))  
print(any(char.isupper() for char in string)) 


#SOLUTION
if __name__ == '__main__':
    s = input()
    
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))