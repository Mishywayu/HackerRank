# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] 
# for a list of students. Print the average of the marks array for the student name provided, 
# showing 2 places after the decimal.

# Example
# marks key:value pairs are 
# 'alpha': [20,30,40]
# 'beta': [30,50,70]
# query_name = 'beta'

# output: 50.0


# ROUGH
data = {
    'shelle':[20,30,40],
    'wayu':[30,50,70]  
}

average = sum(data['wayu']) / len(data['wayu'])
print(f"Average of wayu is: {average:.2f}")

# SOLUTION
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    avg = sum(student_marks[query_name]) / len(student_marks[query_name])
    print(f"{avg:.2f}")