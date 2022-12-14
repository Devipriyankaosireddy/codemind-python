n,count=int(input()),0
l=list(map(int,input().split()))
for i in range(n-1):
    a=l[:i:]
    b=l[i::]
    z=sum(a)+sum(b)
    if(z%2==0):
        print(1)
        break
else:
    print(0)