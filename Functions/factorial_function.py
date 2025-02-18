def factorial(n: int) -> int:
    """
    Calculate factorial of a given number.
    
    The factorial is the product of all integers from 1 to n.
    For 0, factorial returns 1 (by convention).
    
    :param n: The number to calculate factorial of (must be >= 0)
    :return: The factorial of n
    """
    if n <= 1:
        return 1
        
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Test loop for numbers 0-35
for i in range(36):
    print(i, factorial(i))
