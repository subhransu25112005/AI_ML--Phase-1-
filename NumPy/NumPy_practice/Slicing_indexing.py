import numpy as np

# 1D array
arr1 = np.array([10, 20, 30, 40, 50])

print("1D Array:", arr1)

# Indexing
print("First element:", arr1[0])
print("Third element:", arr1[2])

# Slicing
print("Slice (1:4):", arr1[1:4])


# 2D array
arr2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("\n2D Array:\n", arr2)

# 2D Indexing
print("Element [0,1]:", arr2[0,1])
print("Element [2,2]:", arr2[2,2])

# Row extraction
print("First row:", arr2[0])

# Column extraction
print("Second column:", arr2[:,1])

# Sub-array
print("Sub-array (0:2,1:3):\n", arr2[0:2,1:3])

