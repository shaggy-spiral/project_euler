# What is the largest prime factor of the number 600851475143
num = 600851475143
largest = 0
mul = 0
for i in range (1, num + 1):
    for j in range(1, i + 1):
        if (i % j == 0):
            mul += 1
    if (mul == 2):
        if (num % i == 0):
            num = num // i
            print(num)
    mul = 0