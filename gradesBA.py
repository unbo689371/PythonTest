a = int(input('微積分:'))
b = int(input('經濟:'))
c = int(input('組織:'))
d = int(input('企概:'))
e = int(input('國文:'))
f = int(input('英文:'))
g = int(input('會計:'))
mathgrades = [a, b, c, d, e, f, g]
print('七科成績:', end=' ')
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
