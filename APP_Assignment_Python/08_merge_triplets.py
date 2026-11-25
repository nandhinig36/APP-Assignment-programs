def merge_triplets(triplets, target):
    good = [t for t in triplets if all(t[i] <= target[i] for i in range(3))]
    reached = [False] * 3
    for t in good:
        for i in range(3):
            if t[i] == target[i]: reached[i] = True
    return all(reached)

if __name__ == "__main__":
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    print(merge_triplets(triplets, target))
