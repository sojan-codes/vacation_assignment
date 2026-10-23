user_year = int(input("Enter a year: "))
if (user_year % 4 == 0 and user_year % 100 != 0) or user_year % 400 == 0:
    print(user_year, "is leap year.")
else:
    print(user_year, "is not leap year.")