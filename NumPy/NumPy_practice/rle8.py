#🎯 Scenario: ML Model Initialization

import numpy as np

np.random.seed(42)

# Random weights for neural network
weights = np.random.randn(3,3)

# Random input data
input_data = np.random.rand(3,3)

# Random labels (0 or 1)
labels = np.random.randint(0, 2, (3,1))

print("Weights:\n", weights)
print("\nInput Data:\n", input_data)
print("\nLabels:\n", labels)
