#📊 Scenario: Student Subject Analysis

import numpy as np

# rows = students, columns = subjects
marks = np.array([
    [85, 90, 88],
    [78, 82, 80],
    [92, 95, 94]
])

print("Marks:\n", marks)

# Total marks per subject (column-wise)
subject_total = np.sum(marks, axis=0)

# Total marks per student (row-wise)
student_total = np.sum(marks, axis=1)

# Average per subject
subject_avg = np.mean(marks, axis=0)

print("\nSubject Total:", subject_total)
print("Student Total:", student_total)
print("Subject Average:", subject_avg)

