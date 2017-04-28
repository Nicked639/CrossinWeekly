def product(num):
  n = str(num)
  max = 1
  i = 1
  while i < len(n):
      if i == 0:
          p = int(n[0]) * int(n[1:])
      else:
          p = int(n[0:i]) * int(n[i:])
      if max < p:
          max = p
      i += 1
  return max

print(product(12345))