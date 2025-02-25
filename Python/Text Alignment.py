#TASK
# You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
# Your task is to replace the blank (______) with rjust, ljust or center.

# .ljust(width) - This method returns a left aligned string of length width.
# >>> width = 20
# >>> print 'HackerRank'.ljust(width,'-')

# .center(width) - This method returns a centered string of length width.
# >>> width = 20
# >>> print 'HackerRank'.center(width,'-')

# .rjust(width) - This method returns a right aligned string of length width.
# >>> width = 20
# >>> print 'HackerRank'.rjust(width,'-')

# ROUGH 
width = 20
string = 'Michelle'
print(f"This is the string aligned to the left: {string.ljust(width, '.')}")
print(f"This is the string aligned at the center: {string.center(width, '.')}")
print(f"This is the string aligned to the right: {string.rjust(width, '.')}")

# SOLUTION
#Replace all ______ with rjust, ljust or center. 

thickness = 11 #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# #Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# #Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# #Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# #Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))