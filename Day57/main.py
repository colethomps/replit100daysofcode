def reverse(value):
  if value == 1:
      return 1
  else:
      return value * reverse(value - 1)

value = int(input("Input a number: "))
result = reverse(value)
print(f"The factorial of {value} is {result}")
