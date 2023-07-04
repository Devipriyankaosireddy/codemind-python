n=int(input())
b=n*n
last=b%pow(10,len(str(n)))
if (last==n):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")