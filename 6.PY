# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum
sum = 0
squaresum = 0
for i in range (1, 101):
    sum += i
    squaresum += i ** 2 
sum = sum ** 2
print(sum - squaresum)