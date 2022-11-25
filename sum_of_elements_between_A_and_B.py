n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
c=0
for i in l:
    if a<= i <=b:
        c+=i
print(c)