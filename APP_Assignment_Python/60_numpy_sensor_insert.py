import numpy as np

def main():
    readings = np.array([10,20,30,40,50])
    print("Original array:", readings)
    try:
        position = int(input("Insertion position (0 to 5): "))
        raw = input("New integer reading: ")
        if not raw.isdigit(): raise ValueError("Only non-negative integer digits are allowed")
        if not 0 <= position <= len(readings): raise IndexError("Insertion position is out of range")
        readings = np.insert(readings, position, int(raw))
        print("Updated array:", readings)
    except ValueError as error: print("Value error:", error)
    except IndexError as error: print("Index error:", error)
    finally: print("Sensor insertion operation completed.")

if __name__ == "__main__":
    main()
