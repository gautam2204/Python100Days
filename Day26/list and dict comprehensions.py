#square of numbers

num = [2,3,4,5,6,78,9,10]

sq_lst = [i*i for i in num]
print(sq_lst)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [i for i in numbers if i%2==0]

print(result)

list1 = []
list2 = []

with open(file="file1.txt", mode="r") as file:
    list1=file.read().splitlines()

with open(file="file2.txt", mode="r") as file:
    list2=file.read().splitlines()

matching_items = [int(i) for i in list1 if i in list2]
print(matching_items)