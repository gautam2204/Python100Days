student_heightList:list=input("Enter list of student height").split(",")

for height in range(0,len(student_heightList)):
    student_heightList[height] = int(student_heightList[height])

print(student_heightList)

total_height:int = 0
num_students:int = 0
for height in student_heightList:
    total_height+=height
    num_students+=1


print(f"Total height is {total_height}")
print(f"Number of items is {num_students}")
print(f"average of items is {total_height/num_students}")


