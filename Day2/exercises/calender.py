from CalendarModule import *

year = int(input("Input Year: "))
month = int(input("Input Month: "))

print("="*22)
print("       {}  {}".format(year,month))
print("="*22)
print(" Su Mo Tu We Th Fr Sa")
print("="*22)

for i in range(weekDay(year,month,1)):
    print("  ",end="")

for i in range(1,lastDay(year,month)+1):
    print(" %2d" % i, end="")
    if weekDay(year,month,i)==6 and lastDay(year,month) != i:
        print()
print("\n",end=("="*22))