import csv, json, io

CSV_DATA = """name,age,salary
Anita,22,45000
Rahul ,24,52000
Kiran,,40000
Priya,twenty,50000
Meena,25,61000
"""

def clean_csv(data):
    valid = []
    for row in csv.DictReader(io.StringIO(data)):
        row = {key: value.strip() for key, value in row.items()}
        if not row.get("age") or not row.get("salary"): continue
        try:
            valid.append({"name": row["name"], "age": int(row["age"]), "salary": float(row["salary"])})
        except ValueError:
            continue
    return valid

if __name__ == "__main__":
    records = clean_csv(CSV_DATA)
    with open("cleaned_employees.json", "w", encoding="utf-8") as file:
        json.dump(records, file, indent=4)
    print("Cleaned records:", records)
    print("Saved to cleaned_employees.json")
