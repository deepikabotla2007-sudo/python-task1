import random
import math
import numpy as np
import pandas as pd

def generate_data(n):
    students = []

    for i in range(n):
        student_id = f"S{i+1}"
        marks = random.randint(0, 100)
        attendance = random.randint(0, 100)
        assignment = random.randint(0, 50)

        students.append((student_id, marks, attendance, assignment))

    return students


def classify_students(data):
    categories = {
        "At Risk": [],
        "Average": [],
        "Good": [],
        "Top Performer": []
    }

    for student in data:
        sid, marks, attendance, assignment = student

        if marks < 40 or attendance < 50:
            categories["At Risk"].append(sid)

        elif marks > 90 and attendance > 80:
            categories["Top Performer"].append(sid)

        elif 71 <= marks <= 90:
            categories["Good"].append(sid)

        else:
            categories["Average"].append(sid)

    return categories


def analyze_data(data):
    df = pd.DataFrame(data, columns=["ID", "Marks", "Attendance", "Assignment"])

    df["Performance_Index"] = df.apply(
        lambda x: (x["Marks"] * 0.6 + x["Assignment"] * 0.4) * math.log(x["Attendance"] + 1),
        axis=1
    )

    marks_array = df["Marks"].values

    mean_marks = np.mean(marks_array)
    median_marks = np.median(marks_array)
    std_dev = np.std(marks_array)

    max_marks = marks_array[0]
    for m in marks_array:
        if m > max_marks:
            max_marks = m


    min_m = np.min(marks_array)
    max_m = np.max(marks_array)

    df["Normalized_Marks"] = [
        (x - min_m) / (max_m - min_m) if max_m != min_m else 0
        for x in marks_array
    ]


    correlation = np.corrcoef(df["Marks"], df["Attendance"])[0][1]

    consistency = "Consistent" if std_dev < 15 else "Inconsistent"
    attendance_risk = len(df[df["Attendance"] < 50]) > 3
    high_achievement = len(df[df["Marks"] > 90]) >= 2

    if consistency == "Consistent" and not attendance_risk and high_achievement:
        system_status = "Stable Academic System"
    elif attendance_risk:
        system_status = "Critical Attention Required"
    else:
        system_status = "Moderate Performance"

    summary_tuple = (mean_marks, std_dev, max_marks)

    return df, mean_marks, median_marks, std_dev, correlation, summary_tuple, system_status


try:
    n = int(input("Enter number of students: "))
except:
    print("Invalid input! Taking default n = 5")
    n = 5

data = generate_data(n)

categories = classify_students(data)

df, mean_m, median_m, std_dev, corr, summary, status = analyze_data(data)


print("\nDataFrame:\n", df)

print("\nCategories:\n", categories)

print("\nStatistics:")
print("Mean:", mean_m)
print("Median:", median_m)
print("Standard Deviation:", std_dev)
print("Correlation (Marks vs Attendance):", corr)

print("\nSummary Tuple (mean, std_dev, max):", summary)

print("\nFinal System Insight:", status)