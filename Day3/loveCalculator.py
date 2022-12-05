name1 = input("Enter his name...\n").lower()
name2 = input("Enter her name...\n").lower()

combined_name = name1+name2

first_digit=0

first_digit+=combined_name.count("t")
first_digit+=combined_name.count("r")
first_digit+=combined_name.count("u")
first_digit+=combined_name.count("e")

second_digit=0
second_digit+=combined_name.count("l")
second_digit+=combined_name.count("o")
second_digit+=combined_name.count("v")
second_digit+=combined_name.count("e")

total_percent=str(first_digit)+str(second_digit)
print(type(total_percent))
print(f" = {total_percent}")

if int(total_percent)<10 or int(total_percent)>90:
    print(f"Your score is {total_percent}, you go together like coke and mentos.")
else:
    print(f"Your score is {total_percent}.")
