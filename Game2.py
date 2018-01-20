import random
while True:
    ans = random.randint(0, 10)
    for i in range(0, 5):
        guess = int(input())
        if ans == guess:
            print("Bingo!")
            break
        elif ans < guess:
            print("Wrong, is", "less than this value.")
        else:
            print("Wrong, is", "more than this value.")
    print("answer is", ans, "play again?(Y/N)")
    if input() == "N":
        break