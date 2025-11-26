def fibonacci(n: int):
    """
    Generate the Fibonacci sequence up to n terms.

    Args:
        n (int): Number of Fibonacci terms to generate.

    Returns:
        list[int]: List containing the Fibonacci sequence.
    """
    if n <= 0:
        return []
    if n == 1:
        return [0]

    sequence = [0, 1]

    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])

    return sequence


def main():
    try:
        n = int(input("Enter number of Fibonacci terms: "))
        result = fibonacci(n)
        print("Fibonacci sequence:", result)
    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
