n,m=map(int,input().split())
c=0
p=0
for i in range(n,m+1):
    if i%2==0:
        c+=1
    else:
        p+=1
print(c,p)
        