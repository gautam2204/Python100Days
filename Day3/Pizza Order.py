# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1
#
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"
# Your final bill is: $28.

bill = 0
size = input("Enter Pizza Size as 'S' for Small , 'M' for Medium and 'L' for Large")

if size =="S":
    bill = 15
    add_Pepperoni = input("'Y' to add pepperoni\n")
    if add_Pepperoni == "Y":
        bill+=2
    if input("'Y' for extra cheeze") == "Y":
        bill+=1

    print(f"Total Bill = ${bill}")

elif size =="L":
    bill = 25
    add_Pepperoni = input("'Y' to add pepperoni\n")
    if add_Pepperoni == "Y":
        bill += 3
    if input("'Y' for extra cheeze") == "Y":
        bill += 1

    print(f"Total Bill = ${bill}")
