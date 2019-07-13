def leap_year():
    yob = int(input("Please enter your year of birth: "))

    leapyear = (yob % 4 == 0)
    print(str(yob) +' was a leap year:  ' + str(leapyear))
print(leap_year())
