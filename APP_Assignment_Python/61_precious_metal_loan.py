def calculate_interest(metal, purity, amount, tenure):
    rates = {
        "gold": {18: 0.12, 22: 0.10, 24: 0.09},
        "silver": {925: 0.13, 950: 0.12, 999: 0.11},
        "platinum": {900: 0.14, 950: 0.13, 999: 0.12}
    }
    metal = metal.lower()
    if metal not in rates: raise ValueError("Unsupported metal type")
    if purity not in rates[metal]: raise ValueError("Unsupported purity for selected metal")
    if amount <= 0 or tenure <= 0: raise ValueError("Amount and tenure must be positive")
    return amount * rates[metal][purity] * tenure

if __name__ == "__main__":
    try:
        metal = input("Metal (Gold/Silver/Platinum): ")
        purity = int(input("Purity (e.g. 22, 950): "))
        amount = float(input("Loan amount: "))
        tenure = float(input("Tenure in years: "))
        interest = calculate_interest(metal, purity, amount, tenure)
    except TypeError as error: print("Missing argument:", error)
    except ValueError as error: print("Invalid details:", error)
    else: print(f"Simple interest: {interest:.2f}")
    finally: print("Loan calculation process completed.")
