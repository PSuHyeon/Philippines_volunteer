"""
count = 0  		# Global variable

def increment():
    global count  		# Access global variable
    count += 1

def local_example():
    temp = 10 		# Local variable
    print("Local variable:", temp)

increment()
increment()
print("Global variable count:", count)
local_example()




# Exercise
x = 10  # Global scope

def my_function():
    y = 5  # Local scope
    print("Inside the function, y:", y)  
    print("Inside the function, x:", x)  

my_function()
# print(y) 
print("Outside the function, x:", x)  





import math
print("Square root of 16:", math.sqrt(16))

import random
print("Random number between 1 and 10:", random.randint(1, 10))

import os
print("Current working directory:", os.getcwd())





math.sqrt(x)
math.pow(x, y)
math.factorial(x)

math.sin(x)
math.cos(x)
math.tan(x)

math.degrees(x)
math.radians(x)

math.exp(x)
math.log(x)
math.log10(x)

math.pi
math.e


random.random()
random.randint(a, b)
random.uniform(a, b)
random.randrange(start, stop[, step])


import numpy as np

# Create an array and calculate its mean
arr = np.array([1, 2, 3, 4, 5])
mean_value = np.mean(arr)
print("Array:", arr)
print("Mean:", mean_value)

import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Access a column
print("DataFrame:")
print(df)
print("\nAverage Age:", df['Age'].mean())"""

import matplotlib.pyplot as plt

# Data for the plot
months = ['Jan', 'Feb', 'Mar']
sales = [200, 300, 400]

# Create a bar chart
plt.bar(months, sales)
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.show()
