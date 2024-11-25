# Python if, elif, else Statements
### Concept Overview
1. if Statement:
   * Used to execute a block of code only if a specified condition is True.
   * Example:  
   if n % 2 != 0:  
    print("Weird")

2. elif Statement:
   * Stands for "else if."
   * Used after an if statement to check additional conditions if the previous if or elif conditions were False.
   * Only one elif block can execute in a chain, and it stops checking further conditions once a match is found.
   * Example:  
   elif 2 <= n <= 5:  
    print("Not Weird")

3. else Statement:
   * Executes a block of code when all previous if and elif conditions are False.
   * Acts as a "catch-all" for any remaining cases.
   * Example:
   else:  
    print("Not Weird")


### Example: Combining if, elif, and else
if n % 2 != 0:  # Odd numbers  
    print("Weird")  
elif 2 <= n <= 5:  # Even numbers in range 2-5  
    print("Not Weird")  
elif 6 <= n <= 20:  # Even numbers in range 6-20  
    print("Weird")  
else:  # Even numbers greater than 20  
    print("Not Weird")


### Use of and in Conditions
* Combines multiple conditions that must all be True for the block to execute.
* Example:
if n % 2 == 0 and 2 <= n <= 5:  
    print("Not Weird")
* Explanation:
  * n % 2 == 0: Ensures n is even.
  * 2 <= n <= 5: Ensures n is within the range 2 to 5.


## Example: Without and vs With and
### Without and
if n % 2 != 0:  # Check if n is odd  
    print("Weird")  
elif 2 <= n <= 5:  
    print("Not Weird")  
elif 6 <= n <= 20:  
    print("Weird")  
else:  
    print("Not Weird")

* Here, n % 2 == 0 is implicitly assumed after the first if because odd numbers are already excluded.


### With and
if n % 2 != 0:  
    print("Weird")  
elif n % 2 == 0 and 2 <= n <= 5:  
    print("Not Weird")  
elif n % 2 == 0 and 6 <= n <= 20:  
    print("Weird")  
elif n % 2 == 0 and n > 20:  
    print("Not Weird")
