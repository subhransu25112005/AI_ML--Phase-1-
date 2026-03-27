import numpy as np

marks = np.array([85, 90, 78, 92, 88])

print("Marks:", marks)

print("Total Marks:", np.sum(marks))
print("Average Marks:", np.mean(marks))
print("Median Marks:", np.median(marks))
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Performance Variation:", np.std(marks))