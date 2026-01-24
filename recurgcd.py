def Recurgcd(a,b):
    low=min(a,b)
    high=max(a,b)
    if low==0:
        return high
    elif low==1:
        return 1
    else:
        return Recurgcd(low,high%low)
n1=int(input("Enter the number 1:"))
n2=int(input("Enter the number 2:"))
print(Recurgcd(n1,n2))
