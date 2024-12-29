# Import necessary libraries
from ipywidgets import interact
import matplotlib.pyplot as plt

# Function definition: Calculate the square of x and visualize it
def visualize_square(x):
    # Step 1: Calculate the square of x
    # Hint: Multiply x by itself and store the result in the variable y
    y = "~~~~~~~~~~"  # Fill in here (Hint: x * x)

    # Step 2: Set the threshold value
    # Hint: Assign a value to the variable threshold
    threshold = "~~~~~~~~~~"  # Fill in here (Hint: 50)

    # Step 3: Compare x with the threshold
    # Hint: Use if-else to check if x is greater than the threshold
    if "~~~~~~~~~~":  # Fill in here (Hint: x > threshold)
        comparison_result = "~~~~~~~~~~"  # Fill in here (Hint: "greater than")
    else:
        comparison_result = "~~~~~~~~~~"  # Fill in here (Hint: "less than or equal to")

    # Step 4: Visualization
    # Hint: The code below draws the graph. Do not modify it.
    plt.figure(figsize=(6, 4))
    plt.plot([0, x], [0, y], label=f"x: {x}, x²: {y}", marker="o")
    plt.axhline(0, color="gray", linewidth=0.5)
    plt.axvline(0, color="gray", linewidth=0.5)
    plt.xlim(0, 110)
    plt.ylim(0, 11000)
    plt.title(f"Square of [x] (x is {comparison_result} {threshold})")
    plt.xlabel("Input (x)")
    plt.ylabel("Output (x²)")
    plt.legend()
    plt.grid()
    plt.show()

# Step 5: Add interactive functionality
# Hint: Do not modify this part. Simply execute it.
interact(visualize_square, x=(0, 100));
