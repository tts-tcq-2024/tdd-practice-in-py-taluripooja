import re

def add(numbers):
    # Case for empty input
    if numbers == "":
        return 0

    # Handle custom delimiter
    if numbers.startswith("//"):
        delimiter = numbers[2]
        numbers = numbers[4:]  # Skip past the "//" and "\n"
    else:
        delimiter = ","

    # Replace newline with the delimiter for consistent splitting
    numbers = numbers.replace("\n", delimiter)
    
    # Convert to a list of integers, ignoring numbers greater than 1000
    num_list = [int(num) for num in numbers.split(delimiter) if int(num) <= 1000]
    
    # Return the sum of the valid numbers
    return sum(num_list)

