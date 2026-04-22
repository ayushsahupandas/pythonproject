# Q8: Sum of first N natural numbers

n = int(input("Enter value of N: "))

sum = 0
i = 1

while i <= n:
    sum += i
    i += 1

print("Sum of first", n, "natural numbers is:", sum)
