def sum_numbers(*args: float) -> float:
    """
    Calculate the sum of all numbers passed as arguments.
    
    :param args: Variable number of numeric values to sum
    :return: The sum of all provided values
    """
    return sum(args)


# Test cases
print(sum_numbers(1, 2, 3))                # 6
print(sum_numbers(8, 20, 2))               # 30
print(sum_numbers(12.5, 3.147, 98.1))      # 113.747
print(sum_numbers(1.1, 2.2, 5.5))          # 8.8