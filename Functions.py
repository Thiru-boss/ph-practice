#Function: to find the average marks and grade

def find_average_marks(marks):
    sum_of_marks = sum(marks)
    total_subjects = len(marks)
    average_marks = sum_of_marks / total_subjects
    return average_marks

#calculate the grade
def compute_grade(average_marks):
    if average_marks >= 80:
        grade = 'A'
    elif average_marks >= 60:
        grade = 'B'
    elif average_marks >= 50:
        grade = 'c'
    else:
        grade = 'F'
    return grade

marks = [60,65,88,71,59]
average_marks = find_average_marks(marks)
print('average mark:',average_marks)

grade = compute_grade(average_marks)
print('Grade:',grade )