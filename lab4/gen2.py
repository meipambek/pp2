def generator(n):
    if(n%2 == 0):
        for i in range(n+1):  
            if i%2==0:
                yield i
            else:
                yield ', '
    else:
        for i in range(n):  
            if i%2==0:
                yield i
            else:
                yield ', '
n = int(input())        

for i in generator(n):
    print(i ,end='')