# Write your code below this line 👇
def prime_checker(number):
    bool=False
    if number==1:
        bool=True
    for i in range(2,int(number/2)):
        if number%i == 0:
            bool=True
            break

    if bool:
        print(f"Number {number} is not prime")
    else:
        print(f"Number {number} is Prime")

# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
