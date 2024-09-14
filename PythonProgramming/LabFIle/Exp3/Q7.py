# 7.	Write a program which takes any date as input and display next date of the calendar
day = int(input("Enter the day: "))
month = int(input("Enter the month: "))
year = int(input("Enter the year: "))
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    days_in_month[1] = 29
day += 1
if day > days_in_month[month-1]:
    day = 1
    month += 1
    if month > 12:
        month = 1
        year += 1

print(f"The next date is: {day}/{month}/{year}")
