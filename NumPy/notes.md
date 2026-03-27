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

🔹 2. ARRAY CREATION

🧠 What is Array Creation?

👉 Converting data (lists, numbers) into NumPy arrays


---

🔥 1. np.array() (MOST IMPORTANT)

np.array(data)

👉 Converts Python list → NumPy array


---

✅ 1D Array

import numpy as np

arr = np.array([1, 2, 3, 4])
print(arr)

👉 Output:

[1 2 3 4]

👉 This is a 1D array (vector)


---

🔥 2. 2D Array (Matrix)

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])
print(arr2)

👉 Output:

[[1 2 3]
 [4 5 6]]

👉 This is a 2D array (rows + columns)


---

🧠 IMPORTANT RULE (you already learned this!)

❌ Wrong:

np.array([1,2,3], [4,5,6])

✅ Correct:

np.array([[1,2,3], [4,5,6]])

👉 Must use list of lists


---

🔥 3. Nested Lists → Arrays

nested = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

arr = np.array(nested)
print(arr)

👉 Automatically becomes 2D array


---

🧠 Concept Clarity

Structure	Meaning

[1,2,3]	1D array
[[1,2,3],[4,5,6]]	2D array
deeper nesting	higher dimensions



---


🧠 One-line Summary

👉 Array = structured data (1D, 2D, or more)


---

🔹 3. ARRAY PROPERTIES (VERY IMPORTANT)

These tell you everything about an array 🧠


---

🧠 Why this matters?

When working with data:

You must know shape

Type of data

Size


👉 Otherwise → bugs + confusion ❌


---

🔥 1. shape

👉 Tells rows × columns

arr.shape

Example:

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.shape)

👉 Output:

(2, 3)

👉 Meaning:

2 rows

3 columns



---

🔥 2. ndim (number of dimensions)

arr.ndim

Example:

print(arr.ndim)

👉 Output:

2

👉 Meaning:

2D array



---

🔥 3. size

👉 Total number of elements

arr.size

Example:

print(arr.size)

👉 Output:

6

👉 (2 × 3 = 6 elements)


---

🔥 4. dtype

👉 Data type of elements

arr.dtype

Example:

print(arr.dtype)

👉 Output:

int64


---

🧠 Quick Table (REVISION)

Property	Meaning

shape	rows × columns
ndim	number of dimensions
size	total elements
dtype	data type




---

🔹 4. INDEXING & SLICING (VERY IMPORTANT 🔥)

👉 This is how you access and extract data from arrays


---

🧠 Why this matters?

You rarely use full data

You always pick specific parts
👉 That’s indexing & slicing



---

🔥 1. Access Elements (1D)

arr[0]

Example:

import numpy as np

arr = np.array([10, 20, 30, 40])

print(arr[0])   # 10
print(arr[2])   # 30

👉 Index starts from 0


---

🔥 2. Slicing (1D)

arr[start:end]

👉 end is excluded

Example:

print(arr[1:4])   # [20 30 40]


---

🔥 3. 2D Indexing (IMPORTANT)

arr[row, col]

Example:

arr2 = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr2[0,1])   # 2
print(arr2[1,2])   # 6


---

🔥 4. Sub-array Extraction

Row selection:

arr2[0]      # first row

Column selection:

arr2[:,1]    # all rows, column 1

Range selection:

arr2[0:2, 1:3]

👉 Output:

[[2 3]
 [5 6]]


---

🧠 Key Symbols

Symbol	Meaning

:	all elements
,	separate row & column
start:end	range



---
LET’S GOOO 🔥 Now you’re entering a very powerful concept used in ML, data processing, everywhere


---

🔹 5. ARRAY RESHAPING (VERY IMPORTANT)

👉 This is how you change structure of data without changing values


---

🧠 Why this matters?

Data may come in wrong shape

Models need specific shapes
👉 You must reshape data correctly



---

🔥 1. reshape()

arr.reshape(rows, cols)

👉 Changes shape of array


---

✅ Example:

import numpy as np

arr = np.array([1,2,3,4,5,6])

new_arr = arr.reshape(2,3)

print(new_arr)

👉 Output:

[[1 2 3]
 [4 5 6]]


---

⚠️ VERY IMPORTANT RULE

👉 Total elements must match

2 × 3 = 6 ✔️

❌ Wrong:

arr.reshape(3,3)   # Error (needs 9 elements)


---

🔥 2. flatten()

👉 Converts multi-dimensional → 1D array

arr.flatten()

Example:

arr2 = np.array([[1,2,3],[4,5,6]])

flat = arr2.flatten()

print(flat)

👉 Output:

[1 2 3 4 5 6]


---

🔥 3. ravel()

👉 Same as flatten but:

Faster

Returns view (not copy)


arr.ravel()


---

🧠 Difference (important)

Function	Type

flatten()	copy
ravel()	view (faster)



