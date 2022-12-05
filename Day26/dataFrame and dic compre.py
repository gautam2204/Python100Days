students = ["Ram",
            "SAM",
            "jam",
            "can",
            "dan",
            "tan"]
import random

student_scores = {
    student: [random.randint(1, 100),random.randint(1, 100),random.randint(1, 100),random.randint(1, 100)] for student in students
}
print(student_scores)
import pandas as pd

student_dataFrame=pd.DataFrame(student_scores)
print(student_dataFrame)
'''
for (k,v) in student_dataFrame.items():
    print(k)
    print(v)
   '''
rows=student_dataFrame.iterrows()
print(rows)
for row in rows:
    print(row)

for (index,row) in student_dataFrame.iterrows():
    print(row['Ram'])
