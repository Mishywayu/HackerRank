# Given the participants' score sheet for your University Sports Day, 
# you are required to find the runner-up score. You are given n scores. 
# Store them in a list and find the score of the runner-up.

# ROUGH
n = [1,2,3,4,5,7,12,12,1,5,6]

unique_scores = set(n)
print(f"Kinda like the way distinct works in sql: {unique_scores}")

unique_scores.remove(max(unique_scores))
print(f"Runners Up is: {max(unique_scores)}")

# runnerUp = max(n) - 1
# print(f"This was easier: {unnerUp}")

# SOLUTION
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    uniqueScores = set(arr)
    uniqueScores.remove(max(uniqueScores))
    print(max(uniqueScores))