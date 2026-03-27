import numpy as np

arr = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print("Array:\n", arr)

# Sum
print("\nColumn Sum (axis=0):", np.sum(arr, axis=0))
print("Row Sum (axis=1):", np.sum(arr, axis=1))

# Mean
print("\nColumn Mean:", np.mean(arr, axis=0))
print("Row Mean:", np.mean(arr, axis=1))

# Max
print("\nColumn Max:", np.max(arr, axis=0))
print("Row Max:", np.max(arr, axis=1))

