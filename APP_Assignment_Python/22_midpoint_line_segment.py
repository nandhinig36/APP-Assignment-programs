def midpoint(x1, y1, x2, y2):
    return ((x1+x2)/2, (y1+y2)/2)

if __name__ == "__main__":
    x1, y1 = map(float, input("First point x1 y1: ").split())
    x2, y2 = map(float, input("Second point x2 y2: ").split())
    print("Midpoint:", midpoint(x1, y1, x2, y2))
