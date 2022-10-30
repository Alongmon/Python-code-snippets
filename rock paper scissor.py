# rock paper scissor game
import random
while True:
    player = input("Type rock paper or scissor: ").lower()
    computer = int(random.randrange(3))
    r = "rock"
    p = "paper"
    s = "scissor"

    if player == "rock":
        if computer == 0:
            print(f"computer: {r} you: {r}, tied.")
        elif computer == 1:
            print(f"computer: {p} you: {r}, you lost.")
        elif computer == 2:
            print(f"computer: {s} you: {r}, you won.")
    elif player == "paper":
        if computer == 0:
            print(f"computer: {r} you: {p}, you won.")
        elif computer == 1:
            print(f"computer: {p} you: {p}, tied.")
        elif computer == 2:
            print(f"computer: {s} you: {p}, you lost.")

    elif player == "scissor":
        if computer == 0:
            print(f"computer: {r} you: {s}, you lost.")
        elif computer == 1:
            print(f"computer: {p} you: {s}, you won.")
        elif computer == 2:
            print(f"computer: {s} you: {s}, tied.")
    elif player == "quit":
        print("Thank you for playing.")
        break
    else:
        print("Invalid input")
