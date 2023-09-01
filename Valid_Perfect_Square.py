n=int(input())
for i in range(n):
    a=int(input())
    sr=a**0.5
    if sr.is_integer():
        print("True")
    else:
        print("False")