def numbers_down_to_zero(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number (n): "))

print("Numbers from", n, "down to 0:")

for number in numbers_down_to_zero(n):
    print(number)