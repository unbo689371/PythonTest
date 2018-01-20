lower = int(input("輸入區間最小值:"))
upper = int(input("輸入區間最大值:"))

for num in range(lower,upper + 1):

    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            