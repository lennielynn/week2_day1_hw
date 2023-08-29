i = 3
for i in range(2, 100):
    if  i % i + 2  != 0:
      print(i)
    # elif i % i == 0:

       

# num = 0
# while num < 100:
#     print(num)
#     num += 5

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
        for i in range(2, 100):
          if  i % i + 2  != 0:
              print(i)
# print()
        
        
        
#     return num != 1
# for i in range(1, 100):
#     if is_prime(i + 1):
#         print(i + 1)
        
        
        
        
        
        
        