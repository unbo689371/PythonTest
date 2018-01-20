a = int(input('國文:'))
b = int(input('英文:'))
c = int(input('數學:'))
d = int(input('自然:'))
e = int(input('社會:'))
mathgrades = [a, b, c, d, e]
print('五科成績:', end=' ')
for grade in mathgrades:
    print(grade, end=' ')
print(end='\n')

x = sum(mathgrades)
print('總分:', x, end='\n')

average = sum(mathgrades)/len(mathgrades)
print('平均成績:', average)

if average == 60:
    print('Safe！')
elif average < 60:
    print('重修！')
else:
    print('All Pass！')
