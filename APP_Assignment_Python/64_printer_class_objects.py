# Q64: Create three Printer objects and display their identities.
class Printer:
    def __init__(self, capacity, color_mode, printer_type):
        self.capacity = capacity
        self.color_mode = color_mode
        self.printer_type = printer_type

    def display(self):
        print("Print capacity:", self.capacity, "pages per minute")
        print("Color / Mono:", self.color_mode)
        print("Printer type:", self.printer_type)

if __name__ == "__main__":
    printer1 = Printer(20, "Color", "Inkjet")
    printer2 = Printer(35, "Monochrome", "Laser")
    printer3 = Printer(25, "Color", "Laser")

    print("PRINTER 1")
    printer1.display()
    print("Object identity:", id(printer1))
    print("\nPRINTER 2")
    printer2.display()
    print("Object identity:", id(printer2))
    print("\nPRINTER 3")
    printer3.display()
    print("Object identity:", id(printer3))
