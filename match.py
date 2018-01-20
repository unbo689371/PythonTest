import re
print(re.match('wwwww', 'wwwww.runoob.com').span())  # 在起始位置匹配
print(re.match('runoob', 'www.runoob.com'))         # 不在起始位置匹配