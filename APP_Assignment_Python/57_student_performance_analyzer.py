from collections import Counter
from functools import reduce
from datetime import date
import random

students = {
    "Tarun": [82, 91, 78],
    "Karthik": [65, 72, 68],
    "Chadrika": [91, 95, 89],
    "Trisha": [76, 81, 79],
    "Atul": [88, 84, 92]
}

if __name__ == "__main__":
    averages = {}
    all_marks = []
    grade_counter = Counter()

    for student_name, marks in students.items():
        total = 0
        for mark in marks:
            total += mark
            all_marks.append(mark)
        average = total / len(marks)
        averages[student_name] = average
        if average >= 90:
            grade_counter["A"] += 1
        elif average >= 80:
            grade_counter["B"] += 1
        elif average >= 70:
            grade_counter["C"] += 1
        else:
            grade_counter["D"] += 1
        print(student_name, "average:", round(average, 2))

    highest_name = ""
    highest_average = -1
    for student_name, average in averages.items():
        if average > highest_average:
            highest_average = average
            highest_name = student_name

    total_marks = reduce(lambda running_total, mark: running_total + mark, all_marks, 0)
    selected_student = random.choice(list(students.keys()))
    print("Highest average:", highest_name, round(highest_average, 2))
    print("Randomly selected student:", selected_student)
    print("Current date:", date.today().strftime("%d-%m-%Y"))
    print("Grade classification:", grade_counter)
    print("Total marks of all students:", total_marks)
