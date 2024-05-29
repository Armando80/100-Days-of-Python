year = int(input("Enter a year: "))
if year % 4 == 0 and year % 100 != 0:
    print(year, "is a leap year")
elif year % 100 == 0 and year % 400 != 0:
    print(year, "is not a leap year")
elif year % 100 == 0 and year % 400 == 0:
    print(year, "is a leap year")
else:
    print(year, "is not a leap year")
leapYear = str(input("is a leap year? yes or no: "))
if leapYear == "yes":
    secondsYear = int(366 * 86400)
else:
    secondsYear = int(365 * 86400)
print("the year", year, "have", secondsYear, "seconds")