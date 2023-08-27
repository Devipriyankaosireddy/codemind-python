n=int(input())
sqrt_root=n//2
while sqrt_root*sqrt_root>n:
    sqrt_root=(sqrt_root+n//sqrt_root)//2
if sqrt_root*sqrt_root==n:
    print("True")
else:
    print("False")
    