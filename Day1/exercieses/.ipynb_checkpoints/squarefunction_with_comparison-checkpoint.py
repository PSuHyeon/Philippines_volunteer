from ipywidgets import interact
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate square and visualize it
def visualize_square(x):
    y = x * x
    threshold = 50  # Set a threshold for comparison
    comparison_result = "greater than" if x > threshold else "less than or equal to"

    # Create a figure
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

# Add interactivity using interact
interact(visualize_square, x=(0, 100));
