def sumDigits(n):
    if n==0:
        return 0
    else:
        return n % 10+sumDigits(int(n/10))
num=int(input("Enter the number:"))
print(sumDigits(num))    
