# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
div = 0
for i in range (1, 1000000000):    
    div = 0
    for j in range (1, 21):
        if (i % j == 0):
            div += 1
        else:
            break
    if (div == 20):
        print(i)
        break
    else:
        continue