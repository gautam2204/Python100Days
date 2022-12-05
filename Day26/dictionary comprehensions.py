students =[  "Ram",
"SAM",
"jam",
"can",
"dan",
"tan"]


import random

students_scores = {names:random.randint(10,100) for names in students }
print(students_scores)

passed_students = {key:val for (key,val) in students_scores.items() if val>=60}

print(passed_students)
items = students_scores.items()
for i in items:
    print(i)
    print(f"{i[0]} {i[1]}")