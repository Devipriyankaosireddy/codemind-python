n=int(input())
l=list()
a=n
while n>0:
    rem=n%10
    l.append(rem)
    n=n//10
for i in l:
    if l.count(i)>1:
        print("Not Unique Number")
        break
else:
    print('Unique Number')