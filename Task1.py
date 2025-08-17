def factorial(n):
    if n < 0:
        return 
    elif n == 1:
        return 1
    else:
        return n * (factorial(n - 1))

n = int(input("Enter a number: "))
print(f"factorial of {n} is: {factorial(n)}")