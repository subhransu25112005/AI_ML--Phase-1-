import numpy as np

# Fix random values
np.random.seed(0)

# Random float (0 to 1)
rand_arr = np.random.rand(2,3)

# Random integers
int_arr = np.random.randint(1, 10, (2,3))

# Random normal distribution
norm_arr = np.random.randn(2,2)

print("Random Float:\n", rand_arr)
print("\nRandom Integers:\n", int_arr)
print("\nNormal Distribution:\n", norm_arr)
