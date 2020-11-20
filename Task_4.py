number = int(input('Enter a number: '))
start = -1
while number > 10:
    d = number % 10
    number //= 10
    if d > start:
        start = d
print(start)
