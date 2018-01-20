
ans = 7 #猜數字的解答

for guessChance in range(0, 3):
    guess = int(input())
    if ans == guess:
        print('Bingo!')
        break
    else:
        print('猜錯囉')
print('遊戲結束囉')
