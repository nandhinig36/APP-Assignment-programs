import math

def closest_pair(points):
    best = float("inf")
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            x1,y1 = points[i]; x2,y2 = points[j]
            best = min(best, math.hypot(x1-x2, y1-y2))
    return best

if __name__ == "__main__":
    pts = [(0,0),(1,1),(5,5)]
    print("Minimum distance:", closest_pair(pts))
