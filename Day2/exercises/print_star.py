# Print numbers
a = 8
for i in range(a-1):
    if a // 2 > i:
        print(i, (a - 2 * i - 1))

# Right Triangle
a = 8
for i in range(a): 
    print('*' * (i+1))

# Reverse Right Triangle
a = 8
for i in range(a):
    print(" " * (a - (i+1)), end="")
    print('*' * (i+1))
    
# Regular Triangle
a = 8
for i in range(a):
    print(' ' * ((a - 1) - i), end = '')
    print('*' * (2 * i + 1))

# Diamond (1)
a = 11
for i in range(a//2):
    print(' ' * (a//2 - i), end = '')
    print('*' * (2*i+1))

for i in range(a//2-1):
    print(' ' * (i + 2), end = '')
    print('*' * ((a//2*2)-3-2*i))

# Diamond (2)
a = 9
for i in range(a):
    if i <= (a // 2):
        print(" " * (a // 2 - i), end="")
        print("*" * (2 * i + 1))
    else:
        print(" " * (i - a//2), end="")
        print("*" * (a - (2*i - a) - 1))

# Sandglass
a = 8
for i in range(a-1):
    if a // 2 > i:
        print(" " * i, end="")
        print("*" * (a - 2 * i - 1))
    else:
        print(" " * (a - i - 2), end="")
        print("*" * ((2 * i) - a//2 - 1))

# Triple Triangle
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