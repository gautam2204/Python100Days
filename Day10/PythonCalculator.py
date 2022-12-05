from art.calculator_art import logo
from Day10.CalculationsOperations import *
print(logo)
operations_dic={"*":mul,
                "+":add,
                "-":sub,
                "/":div}

num1=int(input("Enter First Number"))


for key in operations_dic:
    print(key)


operation = input("Enter one of the operations from above")
num2=int(input("Enter Second Number"))
calculation = operations_dic[operation]
result = calculation(num1,num2)
print(f"{num1} {operation} {num2} = {result}")
