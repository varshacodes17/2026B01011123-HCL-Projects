import pandas as pd
import numpy as np

# Read Excel file
def perform_analysis(df):
    # Display first 5 students
    print("STUDENT RECORDS")
    print(df.head())

    # Display all columns
    print("\nColumn Names:")
    print(df.columns)

    # Total students
    print("\nTotal Students:", len(df))

    # Average Python marks
    print("\nAverage Python Marks:")
    print(df["Python_Marks"].mean())
    import numpy as np

    # Get Python marks as NumPy array
    marks = np.array(df["Python_Marks"])

    print("\nNUMPY ANALYSIS")

    print("1. Sum:", np.sum(marks))
    print("2. Average:", np.mean(marks))
    print("3. Highest Marks:", np.max(marks))
    print("4. Lowest Marks:", np.min(marks))
    print("5. Standard Deviation:", np.std(marks))

    # Create 1D array
    arr1 = np.array([10, 20, 30, 40, 50])
    print("\n1D Array:", arr1)

    # Create 2D array
    arr2 = np.array([[10, 20], [30, 40]])
    print("2D Array:\n", arr2)
    # NumPy Indexing
    print("\nINDEXING")
    print("First element:", arr1[0])
    print("Third element:", arr1[2])

    # NumPy Slicing
    print("\nSLICING")
    print("First three elements:", arr1[0:3])

    # 2D Array Indexing
    print("\n2D Array Indexing")
    print("Element:", arr2[0, 1])
    # NumPy Indexing
    print("\nINDEXING")
    print("First element:", arr1[0])
    print("Third element:", arr1[2])

    # NumPy Slicing
    print("\nSLICING")
    print("First three elements:", arr1[0:3])

    # 2D Array Indexing
    print("\n2D Array Indexing")
    print("Element:", arr2[0, 1])
    # PANDAS FILTERING

    print("\nSTUDENTS WITH PYTHON MARKS ABOVE 80")

    filtered_data = df[df["Python_Marks"] > 80]

    print(filtered_data)

    # PANDAS SORTING

    print("\nSTUDENTS SORTED BY PYTHON MARKS")

    sorted_data = df.sort_values(
        by="Python_Marks",
        ascending=False
    )

    print(sorted_data.head(10))
    # GROUP BY DEPARTMENT

    print("\nDEPARTMENT WISE AVERAGE MARKS")

    grouped_data = df.groupby("Department")["Python_Marks"].mean()

    print(grouped_data)


    # MISSING VALUES

    print("\nMISSING VALUES")

    print(df.isnull().sum())


    # STATISTICAL ANALYSIS

    print("\nSTATISTICAL ANALYSIS")

    print(df.describe())