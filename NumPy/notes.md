🔹 1. BASICS (NumPy Foundation)


---

🧠 What is NumPy?
👉 NumPy (Numerical Python) is a library used for:
Fast mathematical operations
Working with arrays (like lists but more powerful)


👉 Core object:

ndarray (n-dimensional array)


---

🚀 Why NumPy over Python lists?

❌ Python list problems:

Slow for large data

No vector operations

Memory inefficient


✅ NumPy advantages:

⚡ Faster (written in C)

📦 Less memory

🔥 Supports vectorized operations (no loops needed)



---

🔥 Example (Difference)

# Python list
a = [1,2,3]
b = [4,5,6]

result = []
for i in range(len(a)):
    result.append(a[i] + b[i])

print(result)

👉 NumPy version:

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)   # No loop needed 🔥


---

📥 Importing NumPy

import numpy as np

👉 Why np?

Short

Standard (everyone uses it)



---

🧠 Core Idea You Must Understand

👉 NumPy = array + operations without loops


---

🔥 MASTER PROGRAM (Concept 1)

import numpy as np

# Python list
list1 = [1,2,3]
list2 = [4,5,6]

# NumPy arrays
arr1 = np.array(list1)
arr2 = np.array(list2)

# Operations
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)
print("Square:", arr1 ** 2)


---

🌍 REAL LIFE MASTER PROGRAM

📊 Scenario: Student Marks Analysis

import numpy as np

# marks of 3 subjects
marks = np.array([85, 90, 78])

# bonus marks added
final_marks = marks + 5

# percentage improvement
improvement = (final_marks - marks)

print("Original Marks:", marks)
print("Final Marks:", final_marks)
print("Improvement:", improvement)


---

🧠 What you learned here

NumPy replaces loops

Faster operations

Array-based thinking



---

🔥 Small Practice (DO THIS)

import numpy as np

a = np.array([2,4,6])
b = np.array([1,3,5])

print(a + b)
print(a * b)


---

🧠 One-line Summary

👉 NumPy = Fast array operations without loops


---



