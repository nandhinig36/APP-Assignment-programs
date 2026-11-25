def cumulative_average():
    values = []
    def add_value(number):
        values.append(number)
        return sum(values) / len(values)
    return add_value

if __name__ == "__main__":
    average = cumulative_average()
    while True:
        raw = input("Enter a number (or q to quit): ")
        if raw.lower() == "q": break
        try: print("Cumulative average:", average(float(raw)))
        except ValueError: print("Please enter a valid number.")
