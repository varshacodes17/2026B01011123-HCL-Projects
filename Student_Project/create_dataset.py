import pandas as pd

data = {
    "Roll_No": list(range(101, 151)),
    "Name": [f"Student_{i}" for i in range(1, 51)],
    "Department": ["CSE", "IT", "AI", "ECE", "ME"] * 10,
    "Python_Marks": [78, 85, 90, 67, 88] * 10,
    "Maths_Marks": [80, 75, 95, 70, 82] * 10,
    "Electronics_Marks": [72, 88, 91, 65, 85] * 10
}

df = pd.DataFrame(data)

df.to_excel("students.xlsx", index=False)

print("Excel dataset created successfully!")
print(df.head())
print("Total Students:", len(df))