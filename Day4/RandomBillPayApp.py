import random

string_names = input("Enter names and seperate each name by ', '")

list_of_names = string_names.split(", ")
print(list_of_names)

randomIntNum = random.randint(0, len(list_of_names)-1)

print(list_of_names[randomIntNum])