student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆
'''
Scores 91 - 100: Grade = "Outstanding"

Scores 81 - 90: Grade = "Exceeds Expectations"

Scores 71 - 80: Grade = "Acceptable"

Scores 70 or lower: Grade = "Fail"'''
# TODO-1: Create an empty dictionary called student_grades.
student_grades={}

# TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
    if student_scores[key] <= 70:
        student_scores[key]="Fail"
        student_grades[key]=student_scores[key]
    elif 71<=student_scores[key] <=80:
        student_scores[key]="Acceptable"
        student_grades[key]=student_scores[key]
    elif 81<=student_scores[key] <=90:
        student_scores[key]="Exceeds Expectations"
        student_grades[key]=student_scores[key]
    elif 91<=student_scores[key] <=100:
        student_scores[key]="Outstanding"
        student_grades[key]=student_scores[key]
# 🚨 Don't change the code below 👇
print(student_grades)





