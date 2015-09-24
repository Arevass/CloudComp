total = 2

fib1 = 0
fib2 = 1

while total < 4000000:
  temp = fib1 + fib2
  fib1 = fib2
  fib2 = temp

  total += temp

print total