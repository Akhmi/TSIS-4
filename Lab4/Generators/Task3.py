def divisible_by_3_and_4_generator(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = int(input("Enter a number (n): "))

divisible_by_3_and_4 = divisible_by_3_and_4_generator(n)

print("Numbers divisible by 3 and 4 between 0 and", n, ":", end=" ")
for number in divisible_by_3_and_4:
    print(number, end=", ")