import pandas as pd

from student import (
    display_students,
    search_student,
    add_student,
    update_marks,
    delete_student
)

from reports import generate_report
from analysis import perform_analysis


# Read Excel dataset
df = pd.read_excel("students.xlsx")


while True:

    print("\n===== STUDENT PERFORMANCE SYSTEM =====")
    print("1. Display All Students")
    print("2. Search Student")
    print("3. Add New Student")
    print("4. Update Student Marks")
    print("5. Delete Student")
    print("6. Generate Summary Report")
    print("7. Exit")
    print("8. Perform NumPy and Pandas Analysis")

    choice = input("\nEnter your choice:").strip()
    print("Entered:", repr(choice))

    if choice == "1":

        display_students(df)

    elif choice == "2":

        roll = int(input("Enter Roll Number: "))
        search_student(df, roll)

    elif choice == "3":

        roll = int(input("Enter Roll Number: "))
        name = input("Enter Name: ")
        dept = input("Enter Department: ")

        python = int(input("Enter Python Marks: "))
        maths = int(input("Enter Maths Marks: "))
        electronics = int(input("Enter Electronics Marks: "))

        record = {
            "Roll_No": roll,
            "Name": name,
            "Department": dept,
            "Python_Marks": python,
            "Maths_Marks": maths,
            "Electronics_Marks": electronics
        }

        df = add_student(df, record)
        df.to_excel("students.xlsx", index=False)

        print("Student Added Successfully!")

    elif choice == "4":

        roll = int(input("Enter Roll Number: "))
        marks = int(input("Enter New Python Marks: "))

        df = update_marks(df, roll, marks)
        df.to_excel("students.xlsx", index=False)

        print("Marks Updated Successfully!")

    elif choice == "5":

        roll = int(input("Enter Roll Number: "))

        df = delete_student(df, roll)
        df.to_excel("students.xlsx", index=False)

        print("Student Deleted Successfully!")

    elif choice == "6":

        generate_report(df)

    elif choice == "8":
        perform_analysis(df)
    elif choice == "7":

        print("Thank You!")
        break

    else:

        print("Invalid Choice! Try Again.")