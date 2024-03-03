import time
n = int(input())
millisec = int(input())
root = pow(n, 0.5) 
time.sleep(millisec / 1000)
print("Square root of", n, "after", millisec, "is", root)