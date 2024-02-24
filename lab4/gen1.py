def generator(n):
    for i in range(n+1):
        yield i**2  #i raised to power 2
n = int(input())
for i in generator(n):
    print(i)