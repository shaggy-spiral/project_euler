# What is the largest prime factor of the number 600851475143

dec = 0
reversed = 0
largest = 0
for i in range(100, 1000):
    for j in range (100, 1000):
        num = i * j
        temp = num
        while temp > 0:
            temp = temp // 10
            dec += 1
            inc = 0
        temp = num
        while (dec > 0):
            div = temp // (10 ** (dec-1))
            reversed += div * (10 ** inc) 
            temp = temp % (10 ** (dec-1))
            dec -= 1
            inc += 1
        if (num == reversed):
            if (num > largest):
                largest = num
        dec = 0
        inc = 0
        reversed = 0
print(largest)