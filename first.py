import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Perform some operations
squared = arr ** 2         # Square each element
sum_all = np.sum(arr)      # Sum of all elements
mean_val = np.mean(arr)    # Average of elements

# Print results
print("Original array:", arr)
print("Squared array:", squared)
print("Sum of elements:", sum_all)
print("Mean of elements:", mean_val)