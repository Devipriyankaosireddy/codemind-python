n=int(input())
l=list(map(int,input().split()))
oc=0
for i in range(len(l)):
    oc+=l[i]
average=oc//n
if average in l:
    print("True")
else:
    print("False")