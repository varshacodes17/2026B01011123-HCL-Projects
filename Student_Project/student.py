import pandas as pd

# ==================================
# DATA STRUCTURES
# ==================================

# 1. LIST
student_names = ["Aman", "Riya", "Rahul"]
student_names.append("Priya")
print("Student List:", student_names)

student_names.sort()
print("Sorted List:", student_names)

student_names.remove("Aman")
print("After Removing:", student_names)

# 2. TUPLE
departments = ("CSE", "IT", "AI", "ECE")
print("\nDepartments:", departments)

# 3. SET
unique_departments = {"CSE", "IT", "AI", "CSE"}
print("\nUnique Departments:", unique_departments)

# 4. DICTIONARY
student = {
    "Roll_No": 101,
    "Name": "Aman",
    "Department": "CSE"
}

print("\nStudent Dictionary:", student)
print("Student Name:", student.get("Name"))

# 5. DICTIONARY METHODS
print("Dictionary Keys:", student.keys())
print("Dictionary Values:", student.values())

student.update({"Marks": 90})
print("Updated Dictionary:", student)
print("Dictionary Items:", student.items())


# ==================================
# STUDENT MANAGEMENT FUNCTIONS
# ==================================

# Function 1: Display all students
def display_students(df):
    print(df)


# Function 2: Search student
def search_student(df, roll_no):
    result = df[df["Roll_No"] == roll_no]
    print(result)


# Function 3: Add new student
def add_student(df, record):
    new_data = pd.DataFrame([record])
    df = pd.concat([df, new_data], ignore_index=True)
    return df


# Function 4: Update student marks
def update_marks(df, roll_no, new_marks):
    df.loc[df["Roll_No"] == roll_no, "Python_Marks"] = new_marks
    return df


# Function 5: Delete student
def delete_student(df, roll_no):
    df = df[df["Roll_No"] != roll_no]
    return df