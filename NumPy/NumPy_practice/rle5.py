#📊 Scenario: Salary Calculation System

import numpy as np

# employee salaries
salary = np.array([20000, 30000, 40000])

# bonus (10%)
bonus = salary * 0.10

# updated salary
new_salary = salary + bonus

print("Original Salary:", salary)
print("Bonus:", bonus)
print("New Salary:", new_salary)