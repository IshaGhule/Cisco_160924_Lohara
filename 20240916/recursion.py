def factorial(n):
    # Base case: when n is 0 or 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)

# Example usage
if __name__ == "__main__":
    number = 5
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
