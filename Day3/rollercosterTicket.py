print("Welcome to roller coster")
height = int(input("Enter your height in cms"))
bill = 0

if height > 120:
    age = int(input("Enter Age"))
    if age < 12:
        bill += 5
    elif 12 <= age < 18:
        bill += 7
    else:
        bill += 12

    wantPhoto = input("Enter Y if you want photos and N if not")
    if wantPhoto == "Y":
        bill += 3

    print(f"Yout total bill is ${bill}")


else:
    print("Cannot ride")
