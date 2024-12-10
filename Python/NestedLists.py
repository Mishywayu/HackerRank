# # Given the names and grades for each student in a class of N students, 
# # store them in a nested list and print the name(s) of any student(s) 
# # having the second lowest grade.

# # Note: If there are multiple students with the second lowest grade, 
# # order their names alphabetically and print each name on a new line.

# # ROUGH
# # Input the number of students
# n = 5
# names = ['mishy', 'wayua', 'musembz', 'njoki', 'maryanne']
# scores = [0,0,0,0,0]


# # WORKS RIGHT BUT NOT WHEN THERE IS MORE THAN ONE SECOND LOWEST SCORES
# # unique_scores = sorted(set(scores), reverse=False)  # Remove duplicates and sort scores
# # second_lowest = unique_scores[1]  # Get the second lowest score
# # print(f"This is the second lowest score: {second_lowest}")
# # print(unique_scores)

# # for i in range(n):
# #     sorted_scores = sorted((scores), reverse=False)
# #     print(sorted_scores)
# #     print(f"Student name is {names[i]} and the score is {scores[i]}")

# students = [[names[i], scores[i]] for i in range(n)] #list comprehension
# print (students)
# unique_scores = sorted(set(scores))
# print(unique_scores)

# # find second last score
# if len(unique_scores) > 1:
#     second_lowest_score = unique_scores[1]
# else:
#     print("There is no second lowest score.")
#     exit()

# # Filter students with the second lowest score
# second_lowest_students = [student for student in students if student[1] == second_lowest_score]
# print (second_lowest_students)

# #Sort students alphabetically by name
# second_lowest_students.sort(key=lambda x: x[0])

# #Print names and corresponding scores
# for student in second_lowest_students:
#     print(f"Name: {student[0]}, Score: {student[1]}")



if __name__ == '__main__':
    students =[]
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        
        unique_scores = sorted(set([student[1] for student in students]))
        
        
        if len(unique_scores) > 1:
            second_lowest_score = unique_scores[1]
        else:
            print ("There is no second lowest score.")
        exit()
        
        second_lowest_students = [student for student in students if student[1] == second_lowest_score]
        
        second_lowest_students.sort(key=lambda x: x[0])
        
        for student in second_lowest_students:
            print(f"Name: {student[0]}, Score: {student[1]}")     
        
range = 5
name = ['mishy', 'wayua', 'musembz', 'njoki', 'maryanne']
score = [0,3,3,10,9]

# SOLUTION