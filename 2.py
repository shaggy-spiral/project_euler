# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms
total = 0
before = 0
present = 1
next = 0
while present < 4000000:
    if (present % 2 == 1):
        total += present
    next = present + before
    before = present
    present = next
print(total)