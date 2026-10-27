"""Three Python loop exercises: Collatz sequence, prime check, and multiplication table."""


def collatz_sequence(start):
    if start < 1:
        raise ValueError("starting number must be a positive integer")

    sequence = [start]
    current = start
    while current != 1:
        if current % 2 == 0:
            current //= 2
        else:
            current = current * 3 + 1
        sequence.append(current)
    return sequence


def is_prime(number):
    if number < 2:
        return False
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    return True


def print_multiplication_table(size=10):
    print("\nMultiplication Table:")
    print("   ", end="")
    for column in range(1, size + 1):
        print(f"{column:4}", end="")
    print()

    for row in range(1, size + 1):
        print(f"{row:2} ", end="")
        for column in range(1, size + 1):
            print(f"{row * column:4}", end="")
        print()


def read_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")


def main():
    print("=== Challenge 1: Collatz Conjecture ===")
    start = read_integer("Enter a positive starting number: ")
    try:
        sequence = collatz_sequence(start)
        print("Sequence:", " ".join(map(str, sequence)))
        print("Steps:", len(sequence) - 1)
    except ValueError as error:
        print(f"Invalid input: {error}")

    print("\n=== Challenge 2: Prime Number Checker ===")
    number = read_integer("Enter an integer: ")
    if is_prime(number):
        print(f"{number} is prime.")
    else:
        print(f"{number} is not prime.")

    print("\n=== Challenge 3: Multiplication Table ===")
    print_multiplication_table()


if __name__ == "__main__":
    main()
