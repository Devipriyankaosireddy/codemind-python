s=input()
sum=0
product=1
for i in range(len(s)):
    sum=sum+int(s[i])
    product=product*int(s[i])
    b=product-sum
print(b)