import numpy as np

# 3 students, 3 subjects
marks = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print("Marks:\n", marks)

print("Total Students & Subjects (shape):", marks.shape)
print("Dimension:", marks.ndim)
print("Total Values:", marks.size)
print("Type of Data:", marks.dtype)