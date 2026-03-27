import numpy as np

arr = np.array([10, 25, 30, 15, 5])

print("Original:", arr)

# Boolean indexing
print("Greater than 20:", arr > 20)

# Filtering
print("Filtered (>20):", arr[arr > 20])

# Multiple conditions
print("Between 10 and 30:", arr[(arr > 10) & (arr < 30)])

# Modify values
arr[arr > 20] = 0
print("Modified Array:", arr)