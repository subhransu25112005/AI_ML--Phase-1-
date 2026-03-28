import pandas as pd

# Create data
data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha"],
    "Marks": [85, 90, 78, 92],
    "Subject": ["Math", "Science", "English", "Math"]
}

# Create DataFrame
df = pd.DataFrame(data)

# Step 3: Display data
print("Full Data:")
print(df)

# Step 4: Basic operations
print("\nFirst 2 rows:")
print(df.head(2))

print("\nColumn Names:")
print(df.columns)

print("\nMarks column:")
print(df["Marks"])

# Step 5: Filtering
print("\nStudents with marks > 85:")
print(df[df["Marks"] > 85])

# Step 6: Statistics
print("\nAverage Marks:")
print(df["Marks"].mean())

print("\nMaximum Marks:")
print(df["Marks"].max())