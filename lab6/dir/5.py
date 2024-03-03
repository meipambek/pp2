a = input()
list = [i for i in a.split()]
file = open('/Users/meira/OneDrive/Рабочий стол/pp2/lab6/dir/jjj.txt' , 'w')
for s in list:
    file.write(s + ' ')
file.close
    