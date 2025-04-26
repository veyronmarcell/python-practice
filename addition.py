def sum_list(numbers):
  total = 0
  for num in numbers:
    total += num
    
  return total


numbers = list(map(int,input("Enter numbers separated by spaces: ").split()))
print("sum:",sum_list(numbers))
