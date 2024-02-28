import re
s = input()
x = '^a(b*)$'

if re.search(x,  s):
    print("matches")
else:
    print("Not matches")