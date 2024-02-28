import re
s = input()
x = 'ab{2,3}'
if re.search(x,  s):
    print("matches")
else:
    print("Not matches")