# return true if year is leap year
def isLeapYear(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

# return the last day of month
def lastDay(year,month):
    m = [31,28,31,30,31,30,31,31,30,31,30,31]

    m[1] = 29 if isLeapYear(year) else 28

    return m[month-1]

# return total days from 0001-01-01
def totalDay(year,month,day):
    total = (year-1)*365 + (year-1)//4 - (year-1)//100 + (year-1)//400
    for i in range(1,month):
        total += lastDay(year,i)
    return total + day

# return day of the week (Mon=1, Tue=2, ...)
def weekDay(year,month,day):
    return totalDay(year,month,day) % 7