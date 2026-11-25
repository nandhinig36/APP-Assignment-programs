def probabilities(cards):
    total = len(cards)
    ace = sum(c[:-1] == "A" for c in cards)
    face = sum(c[:-1] in {"J","Q","K"} for c in cards)
    red = sum(c[-1] in {"H","D"} for c in cards)
    black = sum(c[-1] in {"C","S"} for c in cards)
    counts = {"Ace":ace, "Face":face, "Red":red}
    highest = max(counts.values())
    return {k:v/total for k,v in counts.items()}, [k for k,v in counts.items() if v == highest], black/total

if __name__ == "__main__":
    cards = ["AH","10D","KC","QS","2H","JD","7C","KH"]
    probs, most, black = probabilities(cards)
    for key, value in probs.items(): print(f"P({key})={value:.3f}")
    print("Most Frequent Category:", ", ".join(most))
    print(f"P(Black)={black:.3f}")
