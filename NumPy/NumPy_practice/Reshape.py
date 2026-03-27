import numpy as np

# Original array
arr = np.array([1,2,3,4,5,6])

print("Original:", arr)

# Reshape
reshaped = arr.reshape(2,3)
print("\nReshaped (2x3):\n", reshaped)

# Flatten
flat = reshaped.flatten()
print("\nFlatten:", flat)

# Ravel
ravel_arr = reshaped.ravel()
print("\nRavel:", ravel_arr)
