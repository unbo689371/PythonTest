num = int(input("請輸入一個數字："))
factorial = 1

if num < 0:
    print("抱歉，負數沒有階層")
elif num == 0:
    print("0的階層為1")
else:
    for i in range(1,num+1):
        factorial = factorial*i
    print("%d的階層為%d"%(num,factorial))
    