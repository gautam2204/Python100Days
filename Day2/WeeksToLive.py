current_age = input("Enter your current age\n")

years_left = 90 - int(current_age)

days = 365 * years_left
weeks = 52 * years_left
months = 12 * years_left



print(f"You have {days} days, {weeks} weeks, and {months} months left.")