print("Welcome to the tip calculator\n")
total_bill = input("What was your total bill? $")
tip_percent=input("What % tip you will give 10 , 12 or 15? ")
person_count = input("Total number of person to split the bill")

amount_payable_by_each = round((float(total_bill)+((int(tip_percent)/100)*float(total_bill)))/int(person_count),2)
finalAmount="{:.2f}".format(amount_payable_by_each)
print(f"Each person should pay {finalAmount}")

