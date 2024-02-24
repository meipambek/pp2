def generator(n):
    i=0
    while n>=i:
        yield n
        n=n-1
n = int(input())
for i in generator(n):
    print(i)