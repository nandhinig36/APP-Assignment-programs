import random

DEBUG = False 
def play():
    guess = input("Predict heads or tails: ").strip().lower()
    if guess != "heads" and guess != "tails":
        print("Please enter heads or tails.")
        return

    toss = random.choice(["heads", "tails"])
    result = (guess == toss)

    if DEBUG:
        breakpoint()
    print("Your guess:", guess)
    print("Coin toss:", toss)
    print("Correct prediction:", result)
    if result:
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    play()
