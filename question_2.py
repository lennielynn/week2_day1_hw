def prime_num (i):
 for num in range(2, i):
    if i % num == 0:
        return False
    return i != 1
for num in range(1, 100):
    if prime_num (num + 1):
      print(num + 1)
print()

