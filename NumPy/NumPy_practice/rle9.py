#🤖 Scenario: Simple ML Prediction

import numpy as np

# features (input)
X = np.array([2, 3, 4])

# weights
W = np.array([0.5, 1.0, 1.5])

# bias
b = 2

# prediction
prediction = np.dot(X, W) + b

print("Prediction:", prediction)
