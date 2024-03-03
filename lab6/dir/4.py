import os 
path = '/Users/meira/OneDrive/Рабочий стол/pp2/lab6/dir/myFILE.txt'
with open(path, 'r') as ff:
    lines = len(ff.readlines())
    
print(lines)
