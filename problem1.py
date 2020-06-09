import sys


t = int(input().strip())

for a0 in range(t):
    l=[]
    n = int(input().strip())
    for i in range(1,n):
        if(i%3==0 or i%5==0):
            l.append(i)
    print(sum(l))

