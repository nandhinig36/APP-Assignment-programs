def smallest_team(required, people):
    index = {skill:i for i, skill in enumerate(required)}
    target = (1 << len(required)) - 1
    dp = {0: []}
    for person_id, skills in enumerate(people):
        mask = 0
        for skill in skills:
            if skill in index: mask |= 1 << index[skill]
        for covered, team in list(dp.items()):
            combined = covered | mask
            if combined not in dp or len(dp[combined]) > len(team) + 1:
                dp[combined] = team + [person_id]
    return dp[target]

if __name__ == "__main__":
    skills = input("Required skills: ").split()
    count = int(input("Number of candidates: "))
    people = [input(f"Candidate {i} skills: ").split() for i in range(count)]
    print("Selected candidate indices:", *smallest_team(skills, people))
