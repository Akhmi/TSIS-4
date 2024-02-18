def squares_generator(N):
    for i in range(1, N + 1):
        yield i ** 2

N = int(input("Enter a number (N): "))

squares = squares_generator(N)

print("Squares of numbers up to", N, ":")
for square in squares:
    print(square)