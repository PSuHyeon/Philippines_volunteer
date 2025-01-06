# Print numbers
# it would be helpful to determine how to print proper number of * and space in the loop!
a = 8
for i in range(a-1):
    if a // 2 > i:
        print(i, (a - 2 * i - 1))

print("\nRight Triangle (for loop)")
a = 8
for i in range(a): 
    print("*" * (i+1))

print("\nRight Triangel (while loop)")
a = 8
i = 0
while i < a:
    print("*" * (i+1))
    i = i + 1

print("\nReverse Right Triangle (for loop)")
a = 8
for i in range(a):
    print(" " * , end="")
    print("*" * )

print("\nReverse Right Triangle (while loop)")
a = 8
i = 0
while i < a:
    print(" " * , end="")
    print("*" * )
    i = i + 1

print("\nRegular Triangle (for loop)")
a = 8
for i in range(a):
    print(" " * , end = "")
    print("*" * )

print("\nRegular Triangle (while loop)")
a = 8
i = 0
while i < a:
    print(" " * , end = "")
    print("*" * )
    i = i + 1

print("\nDiamond (1) (for loop)")
a = 11
for i in range(a//2):
    print(" " * (a//2 - i), end = "")
    print("*" * (2*i+1))

for i in range(a//2-1):
    print(" " * (i + 2), end = "")
    print("*" * ((a//2*2)-3-2*i))

print("\nDiamond (1) (while loop)")
a = 11
i = 0
while i < (a//2):
    print(" " * (a//2 - i), end = "")
    print("*" * (2*i+1))
    i = i + 1

i = 0
while i < (a//2-1):
    print(" " * (i + 2), end = "")
    print("*" * ((a//2*2)-3-2*i))
    i = i + 1

print("\nDiamond (2) (for loop)")
a = 9
for i in range(a):
    if i <= (a // 2):
        print(" " * (a // 2 - i), end="")
        print("*" * (2 * i + 1))
    else:
        print(" " * (i - a//2), end="")
        print("*" * (a - (2*i - a) - 1))

print("\nDiamond (2) (while loop)")
a = 9
i = 0
while i < a:
    if i <= (a // 2):
        print(" " * (a // 2 - i), end="")
        print("*" * (2 * i + 1))
    else:
        print(" " * (i - a//2), end="")
        print("*" * (a - (2*i - a) - 1))
    i = i + 1

print("\nSandglass (for loop)")
a = 8
for i in range(a-1):
    if a // 2 > i:
        print(" " * i, end="")
        print("*" * (a - 2 * i - 1))
    else:
        print(" " * (a - i - 2), end="")
        print("*" * ((2 * i) - a//2 - 1))

print("\nSandglass (while loop)")
a = 8
i = 0
while i < a-1:
    if a // 2 > i:
        print(" " * i, end="")
        print("*" * (a - 2 * i - 1))
    else:
        print(" " * (a - i - 2), end="")
        print("*" * ((2 * i) - a//2 - 1))
    i = i + 1

print("\nTriple Triangle (for loop)")
a = 8
for i in range(a):
    if i < (a//2):
        for x in range(a-i):
            print(" ", end="")
        for x in range(i*2+1):
            print("*", end="")
    else:
        for x in range(a - i):
            print(" ", end="")
        for x in range(i*2+1 - a):
            print("*", end="")
        for x in range(a - (i*2+1 - a)):
            print(" ", end="")
        for x in range(i*2+1 - a):
            print("*", end="")
    print()

print("\nTriple Triangle (while loop)")
a = 8
i = 0
while i < a:
    if i < (a//2):
        j = 0
        while j < (a-i):
            print(" ", end="")
            j = j + 1
        j = 0
        while j < (i*2+1):
            print("*", end="")
            j = j + 1
    else:
        j = 0
        while j < (a - i):
            print(" ", end="")
            j = j + 1
        j = 0
        while j < (i*2+1 - a):
            print("*", end="")
            j = j + 1
        j = 0
        while j < (a - (i*2+1 - a)):
            print(" ", end="")
            j = j + 1
        j = 0
        while j < (i*2+1 - a):
            print("*", end="")
            j = j + 1
    i = i + 1
    print()