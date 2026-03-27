import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

# Element-wise multiplication
print("Element-wise:", a * b)

# Broadcasting
print("Broadcasting (a * 2):", a * 2)

# Dot product
print("Dot Product:", np.dot(a, b))


# 2D example
arr = np.array([
    [1,2],
    [3,4]
])

print("\n2D Broadcasting:\n", arr + 5)

b2 = np.array([
    [5,6],
    [7,8]
])

print("\nMatrix Multiplication:\n", arr @ b2)

