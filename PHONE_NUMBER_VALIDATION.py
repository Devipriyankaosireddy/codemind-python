n=int(input())
s=str(n)
l=list(map(int,s))
if len(l)<10:
    print("Invalid")
else:
    print("Valid")