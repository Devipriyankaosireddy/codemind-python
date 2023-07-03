s=input()
sum=0
product=1
for i in range(len(s)):
    sum=sum+int(s[i])
    product=product*int(s[i])
if (sum==product):
    print("Spy Number")
else:
    print("Not Spy Number")