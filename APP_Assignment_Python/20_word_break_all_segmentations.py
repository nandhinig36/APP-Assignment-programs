def word_break(s, word_dict):
    words = set(word_dict)
    memo = {}
    def build(start):
        if start == len(s): return [""]
        if start in memo: return memo[start]
        answers = []
        for end in range(start + 1, len(s) + 1):
            word = s[start:end]
            if word in words:
                for suffix in build(end):
                    answers.append(word + (" " + suffix if suffix else ""))
        memo[start] = answers
        return answers
    return build(0)

if __name__ == "__main__":
    s = input("String: ")
    words = input("Dictionary words: ").split()
    answers = word_break(s, words)
    print("Can Segment:", bool(answers))
    print("Segmentations:")
    print("\n".join(answers) if answers else "None")
