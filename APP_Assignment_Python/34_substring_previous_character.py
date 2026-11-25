def transform(s, sub):
    start = s.find(sub)
    if start == -1: raise ValueError("sub must be a contiguous part of s")
    changed = "".join("z" if ch == "a" else chr(ord(ch)-1) for ch in sub)
    return s[:start] + changed + s[start+len(sub):]

if __name__ == "__main__":
    s = input("String: "); sub = input("Substring: ")
    print(transform(s, sub))
