# You are given a string and your task is to swap cases. 
# In other words, convert all lowercase letters to uppercase letters and vice versa.

# Example:
# Www.HackerRank.com → wWW.hACKERrANK.COM
# Pythonist 2 → pYTHONIST 2 

# ROUGH
myString = "MICHelle"
# print(myString)
print(myString.swapcase()) #works

# for i in range(len(myString)):
#     print(i) #oopps, that's for indexes

#using for loop though
res = ""
for i in myString:
    if i.isupper():
        res += i.lower()
    if i.islower():
        res += i.upper()
print("This is result using a for loop: " + res)