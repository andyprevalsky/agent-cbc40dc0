"""Compute and print the Collatz sequence starting from 27."""


def collatz(n: int) -> list[int]:
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence


def main() -> None:
    sequence = collatz(27)
    for value in sequence:
        print(value)
    total_steps = len(sequence) - 1
    print(f"Total steps: {total_steps}")


if __name__ == "__main__":
    main()
