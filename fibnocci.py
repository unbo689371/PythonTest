nterms = int(input("你需要幾項?"))

n1 = 0
n2 = 1
count = 2

if nterms <=0:
    print("請輸入一個正整數。")
elif nterms == 1:
    print("婓波那契數列:")
    print(n1)
else:
    print("斐波那契数列：")
    print(n1,",",n2,end=" , ")
    while count < nterms:
        nth = n1 + n2
        print(nth,end=" , ")

        n1 = n2
        n2 = nth
        count += 1
        
