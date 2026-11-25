from collections import defaultdict
from itertools import combinations
from functools import reduce
from datetime import date
import random
import math
import sys

STUDENTS = [
    ("Anita", 85, "CSE"), ("Rahul", 78, "CSE"), ("Priya", 92, "CSE"),
    ("Kiran", 80, "CSE"), ("Nandhini", 90, "AI"), ("Vijay", 76, "AI"),
    ("Meera", 91, "AI"), ("Arun", 82, "Data Science"),
    ("Divya", 88, "Data Science"), ("Kavya", 79, "Data Science"),
    ("Rohan", 86, "Cyber Security"), ("Isha", 93, "Cyber Security")
]

def allocate(team_size):
    if team_size < 1:
        raise ValueError("Team size must be at least 1")
    department_groups = defaultdict(list)
    for student in STUDENTS:
        department_groups[student[2]].append(student)

    
    all_teams = []
    for department, members in department_groups.items():
        if len(members) >= team_size:
            department_teams = list(combinations(members, team_size))
            for team in department_teams:
                all_teams.append((department, team))
    if len(all_teams) == 0:
        raise ValueError("No department has enough students for this team size")

    selected_department, selected_team = random.choice(all_teams)
   
    total = reduce(lambda running_total, person: running_total + person[1], selected_team, 0)
    average = math.ceil(total / team_size * 100) / 100
    return selected_department, selected_team, total, average

if __name__ == "__main__":
    if len(sys.argv) > 1:
        team_size = int(sys.argv[1])
    else:
        team_size = int(input("Enter team size: "))
    department, team, total, average = allocate(team_size)
    print("===== PROJECT TEAM ALLOCATION =====")
    print("Team Size:", team_size)
    print("Allocation Date:", date.today().strftime("%d-%m-%Y"))
    print("Department:", department)
    print("Selected Team:")
    for number, student in enumerate(team, 1):
        print(str(number) + ".", student[0], "-", student[1])
    print("Total Marks:", total)
    print("Average Marks:", format(average, ".2f"))
