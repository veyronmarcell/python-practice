def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

# test
n = int(input("Pick a number: "))
print("Its factorial is:", factorial(n))
