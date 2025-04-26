def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

# Example 
num = int(input("Enter a number: "))
print("Sum of digits:", sum_of_digits(num))
