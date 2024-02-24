def generator(n,k):
    for i in range(n,k):  
        yield i**2
n = int(input())
k = int(input())

for i in generator(n, k):
    print(i)