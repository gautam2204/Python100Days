num_lst = [1, 2, 2, 4, 6, 5, 4, 1]

dict_of_num = {}

for num in num_lst:
    if not dict_of_num.keys().__contains__(num):
        dict_of_num[num] = 1
    else:
        dict_of_num[num] = dict_of_num[num] + 1

print(dict_of_num)

for (k, v) in dict_of_num.items():
    print(dict_of_num.items())
    if v >= 2:
        print(f"value is repeated {k}")

for item in dict_of_num.items():
    if item[1] >= 2:
        print(f"via tuple {item[0]}")

my_str = "Java2Jee"  #j=2,a=2,e=2

my_str.upper()