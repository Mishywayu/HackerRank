# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.

# ROUGH
def capitalized():
    uncapitalized_name = "michelle"
    uncapitalized_fullname = "michelle muindi"

    capitalized_name = uncapitalized_name.capitalize()
    capitalized_fullname = uncapitalized_fullname.title()

    print(f"This is the capitalized name: {capitalized_name} and this is the capitalized fullname: {capitalized_fullname}")

capitalized()

# SOLUTION
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    return s.title()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()