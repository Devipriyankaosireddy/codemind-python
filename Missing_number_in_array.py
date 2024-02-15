t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    c=0
    for j in range(1,n+1):
        if j not in l:
            print(j)
    
            