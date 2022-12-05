row1 = ["", "", ""]
row2 = ["", "", ""]
row3 = ["", "", ""]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

map[2][1] = "XX"
print(map)
print(f"{row1}\n{row2}\n{row3}")
