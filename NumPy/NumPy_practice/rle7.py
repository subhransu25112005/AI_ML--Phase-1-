#📊 Scenario: ML Data Initialization

import numpy as np

# initialize weights (zeros)
weights = np.zeros((3,3))

# initialize bias (ones)
bias = np.ones((3,1))

# create input range
data_points = np.linspace(0, 1, 5)

print("Weights:\n", weights)
print("\nBias:\n", bias)
print("\nInput Data:", data_points)