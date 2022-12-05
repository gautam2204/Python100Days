number_list:list=input("Enter numbers").split(",")

for i in range(0,len(number_list)):
    number_list[i] = int(number_list[i])

print(f"Number List Entered is \n{number_list}")
print(f"Using default method\nmax number ={max(number_list)}\nmin number ={min(number_list)}")

print("Now, by for loop logic")

max_num = 0
min_num=0
for i in number_list:
    if i>max_num:
        max_num=i

  #  if i<min_num:
  #      min_num=i
print(f"Using for loop\nmax number ={max_num}\nmin number ={min_num}")

