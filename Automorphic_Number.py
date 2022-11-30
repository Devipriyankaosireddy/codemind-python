n=int(input())
l=len(str(n))
s=n**2
au=s%pow(10,len(str(n)))
if au==n:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")