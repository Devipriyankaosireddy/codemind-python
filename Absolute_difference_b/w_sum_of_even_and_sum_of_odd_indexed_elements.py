n=int(input())
lst=list(map(int,input().split()))
oc,ec=0,0
for i in range(len(lst)):
    if i%2==0:
        oc+=lst[i]
    else:
        ec+=lst[i]
print(abs(ec-oc))
