def generate_parentheses(n):
    result = []
    def backtrack(current, opened, closed):
        if len(current) == 2*n:
            result.append(current); return
        if opened < n: backtrack(current+"(", opened+1, closed)
        if closed < opened: backtrack(current+")", opened, closed+1)
    backtrack("", 0, 0)
    return result

if __name__ == "__main__":
    print(generate_parentheses(int(input("Number of pairs: "))))
