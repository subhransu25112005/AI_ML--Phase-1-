import pandas as pd

# Step 1: Create a sample CSV (run once)
data = {
    "Name": ["Aman", "Riya", "Rahul", "Sneha", "Karan"],
    "Marks": [85, 90, 78, 92, 67],
    "City": ["Delhi", "Mumbai", "Delhi", "Kolkata", "Mumbai"]
}

df = pd.DataFrame(data)
df.to_csv("students.csv", index=False)

# Step 2: Read CSV file
df = pd.read_csv("students.csv")

print("Full Data:")
print(df)

# Step 3: Filter data
print("\nStudents from Delhi:")
print(df[df["City"] == "Delhi"])

# Step 4: Sorting
print("\nSorted by Marks (High to Low):")
print(df.sort_values(by="Marks", ascending=False))

# Step 5: Value count
print("\nCity Count:")
print(df["City"].value_counts())

# Step 6: Add new column
df["Status"] = df["Marks"].apply(lambda x: "Pass" if x >= 75 else "Fail")

print("\nUpdated Data:")
print(df)