import pandas as pd

def generate_report(df):

    print("\n===== STUDENT PERFORMANCE REPORT =====")

    # Total Students
    print("Total Students:", len(df))

    # Average Marks
    print("\nAverage Python Marks:",
          df["Python_Marks"].mean())

    print("Average Maths Marks:",
          df["Maths_Marks"].mean())

    print("Average Electronics Marks:",
          df["Electronics_Marks"].mean())

    # Highest and Lowest Marks
    print("\nHighest Python Marks:",
          df["Python_Marks"].max())

    print("Lowest Python Marks:",
          df["Python_Marks"].min())

    # Department Wise Count
    print("\nDepartment Wise Student Count:")
    print(df["Department"].value_counts())

    # Student Insights
    print("\n===== STUDENT INSIGHTS =====")

    top_student = df.loc[df["Python_Marks"].idxmax()]

    print("Top Performer:", top_student["Name"])
    print("Top Performer's Marks:", top_student["Python_Marks"])

    department_avg = df.groupby("Department")["Python_Marks"].mean()

    print("\nDepartment Average Marks:")
    print(department_avg)

    print("\nHighest Performing Department:")
    print(department_avg.idxmax())

    print("\n===== REPORT GENERATED =====")