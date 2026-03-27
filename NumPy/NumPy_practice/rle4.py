#📊 Scenario: Image Data Processing

import numpy as np

# Suppose image pixels (2x3 image)
image = np.array([
    [255, 128, 64],
    [0, 100, 200]
])

print("Original Image:\n", image)

# Convert image to 1D (for ML model input)
flat_image = image.flatten()
print("\nFlattened Image:", flat_image)

# Reshape back to original
reshaped_image = flat_image.reshape(2,3)
print("\nReshaped Image:\n", reshaped_image)