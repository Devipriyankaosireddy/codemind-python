n=int(input())
l=list(map(int,input().split())) #2 8 3 4
m=0
for i in range(1,n+1): #2
    if i not in l:#i=2
        m+=i
for i in l:
    p=l.count(i)
    if p>1:
        print(i,m)
        break
        
        