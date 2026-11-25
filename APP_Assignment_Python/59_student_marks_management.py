class InvalidMarksError(Exception):
    pass

def main():
    while True:
        try:
            name = input("Student name: ").strip()
            assert name, "Student name cannot be empty"
            marks = float(input("Marks (0-100): "))
            if not 0 <= marks <= 100: raise InvalidMarksError("Marks must be between 0 and 100")
            with open("student_records.txt", "a", encoding="utf-8") as file:
                file.write(f"{name},{marks:g}\n")
            print("Record saved.")
        except AssertionError as error: print("Name error:", error)
        except ValueError: print("Marks must be numeric.")
        except InvalidMarksError as error: print("Invalid marks:", error)
        finally: print("Record processing completed.")
        if input("Add another? (y/n): ").lower() != "y": break

if __name__ == "__main__":
    main()
