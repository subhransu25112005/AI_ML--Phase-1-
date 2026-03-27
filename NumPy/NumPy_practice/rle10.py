
#📊 Scenario: Student Result Filtering

import numpy as np

marks = np.array([85, 40, 90, 55, 30])

print("Marks:", marks)

# Pass students (>=50)
passed = marks[marks >= 50]

# Fail students (<50)
failed = marks[marks < 50]

# Replace failed marks with 0
marks[marks < 50] = 0

print("Passed:", passed)
print("Failed:", failed)
print("Updated Marks:", marks)

