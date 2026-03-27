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



LET’S GO 🔥🔥
Now you’re entering the REAL POWER of NumPy 💪


---

🔹 6. MATHEMATICAL OPERATIONS

👉 This is why NumPy exists
👉 No loops → direct operations on arrays


---

🧠 Core Idea

👉 Operations happen element-wise


---

🔥 1. Element-wise Operations

arr1 + arr2
arr1 - arr2
arr1 * arr2
arr1 / arr2


---

✅ Example:

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a + b)   # [5 7 9]
print(a * b)   # [4 10 18]

👉 Each element operates position-wise


---

🔥 2. Array vs Scalar Operations

arr + 5
arr * 2


---

Example:

a = np.array([10,20,30])

print(a + 5)   # [15 25 35]
print(a * 2)   # [20 40 60]

👉 Scalar applies to every element


---

🔥 3. Array vs Array Operations

👉 Arrays must have same shape

a + b
a * b


---

Example:

a = np.array([2,4,6])
b = np.array([1,3,5])

print(a + b)   # [3 7 11]
print(a - b)   # [1 1 1]


---

⚠️ Important Rule

👉 Shapes must match (for now)

(3,) + (3,) ✔️
(3,) + (2,) ❌

(We’ll fix this later using broadcasting 🔥)


LET’S GOOO 🔥🔥
Now you’re stepping into data analysis power zone 📊💪


---

🔹 7. STATISTICAL FUNCTIONS

👉 These functions help you analyze data quickly
👉 Used in ML, Data Science, Analytics


---

🧠 Why this matters?

Instead of writing long logic: 👉 NumPy gives ready-made statistical tools


---

🔥 1. np.sum()

👉 Total of all elements

np.sum(arr)

Example:

import numpy as np

arr = np.array([10, 20, 30])

print(np.sum(arr))   # 60


---

🔥 2. np.mean()

👉 Average value

np.mean(arr)

Example:

print(np.mean(arr))   # 20.0


---

🔥 3. np.median()

👉 Middle value (sorted)

np.median(arr)


---

🔥 4. np.max() & np.min()

👉 Maximum & Minimum

np.max(arr)
np.min(arr)


---

🔥 5. np.std()

👉 Standard deviation (spread of data)

np.std(arr)


---

🧠 Concept Insight

Function	Meaning

sum	total
mean	average
median	middle
max/min	highest/lowest
std	variation



---

LET’S GO 🔥🔥
Now you’re learning SUPER IMPORTANT NumPy tools used everywhere 💯


---

🔹 8. SPECIAL ARRAYS (VERY IMPORTANT 🔥)

👉 These are pre-built array generators
👉 Used in ML, simulations, testing, etc.


---

🧠 Why this matters?

Instead of manually writing arrays: 👉 NumPy creates them instantly


---

🔥 1. np.zeros()

👉 Creates array filled with 0

np.zeros((rows, cols))

Example:

import numpy as np

print(np.zeros((2,3)))

👉 Output:

[[0. 0. 0.]
 [0. 0. 0.]]


---

🔥 2. np.ones()

👉 Creates array filled with 1

np.ones((rows, cols))


---

🔥 3. np.eye()

👉 Identity matrix (diagonal = 1)

np.eye(n)

Example:

print(np.eye(3))

👉 Output:

[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]


---

🔥 4. np.arange()

👉 Range with step

np.arange(start, end, step)

Example:

print(np.arange(1, 10, 2))

👉 Output:

[1 3 5 7 9]


---

🔥 5. np.linspace()

👉 Equal spacing based on number of values

np.linspace(start, end, count)

Example:

print(np.linspace(1, 10, 5))

👉 Output:

[ 1.   3.25  5.5   7.75 10. ]


---

🧠 Important Difference (VERY IMPORTANT 🔥)

Function	Works on

arange	step
linspace	number of values



---
LET’S GOOO 🔥🔥
Now you’re entering AI/ML CORE territory 🎯


---

🔹 9. RANDOM MODULE (VERY IMPORTANT 🔥)

👉 Used to generate random data
👉 Essential for:

Machine Learning 🤖

Simulations 🎲

Testing 📊



---

🧠 Why this matters?

Real-world data is unpredictable
👉 So we simulate it using random numbers


---

🔥 1. np.random.rand()

👉 Generates random numbers (0 to 1)

np.random.rand(rows, cols)


---

✅ Example:

import numpy as np

print(np.random.rand(2,3))

👉 Output (random):

[[0.12 0.85 0.43]
 [0.67 0.21 0.99]]


---

🔥 2. np.random.randint()

👉 Random integers

np.random.randint(start, end, size)


---

Example:

print(np.random.randint(1, 10, (2,3)))

👉 Output:

[[3 7 1]
 [9 2 5]]


---

🔥 3. np.random.randn()

👉 Random numbers from normal distribution (mean=0, std=1)

np.random.randn(rows, cols)


---

Example:

print(np.random.randn(2,2))

👉 Output:

[[ 0.45 -1.23]
 [ 0.67  0.12]]


---

🧠 Important Concept

Function	Range

rand	0 → 1
randint	integers
randn	normal distribution



---

⚠️ Important (VERY USEFUL)

Same random values every time:

np.random.seed(0)

👉 Fixes randomness (used in ML experiments)


---

LET’S GOOO 🔥🔥
Now you’re entering CORE NUMPY POWER 💪


---

🔹 10. ARRAY OPERATIONS (VERY IMPORTANT 🔥🔥)

👉 This is where NumPy becomes super powerful


---

🧠 What you’ll learn

Broadcasting

Element-wise multiplication

Dot product



---

🔥 1. ELEMENT-WISE MULTIPLICATION

👉 Same shape → multiply position-wise

a * b

Example:

import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

print(a * b)   # [4 10 18]


---

🔥 2. BROADCASTING (VERY IMPORTANT ⚡)

👉 Different shapes → NumPy automatically adjusts


---

🧠 Rule (simple understanding)

👉 Smaller array is expanded to match bigger one


---

Example:

a = np.array([1,2,3])
b = 2

print(a * b)   # [2 4 6]

👉 Scalar becomes:

[2 2 2]


---

🔥 2D Broadcasting Example

arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr + 10)

👉 Output:

[[11 12 13]
 [14 15 16]]


---

⚠️ Broadcasting Rule (IMPORTANT)

Shapes must be compatible:

(3,) + (3,) ✔️  
(2,3) + (3,) ✔️  
(2,3) + (2,) ❌


---

🔥 3. DOT PRODUCT (VERY IMPORTANT 💥)

👉 Used in:

Machine Learning

Neural Networks

Matrix multiplication



---

Syntax:

np.dot(a, b)
# or
a @ b


---

Example:

a = np.array([1,2,3])
b = np.array([4,5,6])

print(np.dot(a,b))   # 32

👉 Calculation:

1×4 + 2×5 + 3×6 = 32


---

🔥 2D Dot Product

a = np.array([
    [1,2],
    [3,4]
])

b = np.array([
    [5,6],
    [7,8]
])

print(a @ b)

👉 Output:

[[19 22]
 [43 50]]


---

LET’S GOOO 🔥🔥
Now you’re learning how to filter and control data like a pro 🔍💪


---

🔹 11. CONDITIONAL OPERATIONS (VERY IMPORTANT 🔥)

👉 This is used to select specific data based on conditions


---

🧠 Why this matters?

Real-world data:

You don’t use everything

You filter useful parts


👉 Example:

Marks > 90

Salary > 50k

Values < threshold



---

🔥 1. BOOLEAN INDEXING

👉 Condition returns True / False

arr > 5


---

Example:

import numpy as np

arr = np.array([2,5,8,1,9])

print(arr > 5)

👉 Output:

[False False  True False  True]


---

🔥 2. FILTERING ARRAYS

👉 Extract only values that satisfy condition

arr[arr > 5]


---

Example:

print(arr[arr > 5])

👉 Output:

[8 9]


---

🔥 3. MULTIPLE CONDITIONS

(arr > 2) & (arr < 9)

⚠️ Use:

& → AND

| → OR



---

Example:

print(arr[(arr > 2) & (arr < 9)])

👉 Output:

[5 8]


---

🔥 4. MODIFY USING CONDITION

arr[arr > 5] = 0


---

Example:

arr[arr > 5] = 0
print(arr)

👉 Output:

[2 5 0 1 0]


---

🧠 Key Operators

Operator	Meaning

>	greater
<	less
==	equal
&	AND
`	`



---

LET’S GOOOO 🔥🔥


---

🔹 12. AXIS CONCEPT (VERY IMPORTANT 🔥🔥)

👉 This controls HOW operations are applied in 2D arrays


---

🧠 Core Idea

👉 Axis tells NumPy:

> “Apply operation across rows OR columns?”




---

🔥 Visual Understanding

Think of a table:

[ [1, 2, 3],
  [4, 5, 6] ]


---

🔥 axis = 0 (COLUMN-wise)

👉 Move down (vertical)
👉 Operate on columns

np.sum(arr, axis=0)

👉 Calculation:

[1+4, 2+5, 3+6] = [5, 7, 9]


---

🔥 axis = 1 (ROW-wise)

👉 Move across (horizontal)
👉 Operate on rows

np.sum(arr, axis=1)

👉 Calculation:

[1+2+3, 4+5+6] = [6, 15]


---

🧠 Easy Memory Trick

Axis	Meaning

axis=0	↓ down → columns
axis=1	→ across → rows



---

🔥 Functions with Axis

You can use axis in:

np.sum()

np.mean()

np.max()

np.min()



---

✅ Example:

import numpy as np

arr = np.array([
    [10,20,30],
    [40,50,60]
])

print("Column Sum:", np.sum(arr, axis=0))
print("Row Sum:", np.sum(arr, axis=1))


---



👉 Axis decides direction of operation (row vs column)


---

🎯 FINAL RESULT

 covered:

✅ NumPy basics
✅ Array creation
✅ Properties
✅ Indexing
✅ Reshaping
✅ Math operations
✅ Statistics
✅ Special arrays
✅ Random
✅ Broadcasting + Dot
✅ Conditions
✅ Axis


