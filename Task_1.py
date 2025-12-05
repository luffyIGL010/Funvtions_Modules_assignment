# Calculate the Factorial of a Number

def Fact(n):
    if n==1:
        return 1
    else:
        return n*Fact(n-1)

        
num=int(input("Enter a number: "))

Fact(num)
print(f"Factorial of {num} is {Fact(num)}")
        