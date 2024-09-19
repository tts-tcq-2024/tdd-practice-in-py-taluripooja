import re

class StringCalculator:
    def __init__(self, check_function, result_function):
        self.check_function = check_function
        self.result_function = result_function
        self.enabled = False

def check_empty_input(input_str):
    return 1 if input_str == "" or input_str is None else 0

def check_for_negative_input(input_str):
    return 1 if '-' in input_str else 0

def print_exception_if_negative_number(numbers):
    tokens = numbers.split(',')
    negatives = [int(token) for token in tokens if int(token) < 0]
    if negatives:
        print(f"Negative number found: {', '.join(map(str, negatives))}")

def extract_actual_delimiter(delimiter):
    if delimiter.startswith('[') and delimiter.endswith(']'):
        return delimiter[1:-1]
    return delimiter

def replace_delimiter_with_comma(input_str, delimiter):
    actual_delimiter = extract_actual_delimiter(delimiter)
    return input_str.replace(actual_delimiter, ',')

def check_newline_delimiter_and_replace_with_comma(input_str):
    if '\n' in input_str:
        return replace_delimiter_with_comma(input_str, '\n')
    return input_str

def check_for_custom_delimiter_and_replace_with_comma(input_str):
    if input_str.startswith('//'):
        delimiter_end = input_str.index('\n')
        delimiter = input_str[2:delimiter_end]
        modified_input = input_str[delimiter_end+1:]
        return replace_delimiter_with_comma(modified_input, delimiter)
    return input_str

def ignore_numbers_greater_than_1000(num):
    return num if num <= 1000 else 0

def sum_numbers(numbers):
    tokens = numbers.split(',')
    total = sum(ignore_numbers_greater_than_1000(int(token)) for token in tokens if token.isdigit())
    return total

def return_zero_for_empty_input(numbers):
    return 0

def return_sum_if_default_delimiter(numbers, return_value):
    if return_value == 0:
        return sum_numbers(numbers)

def add(numbers):
    if numbers is None:
        numbers = ""

    modified_numbers = numbers

    calculators = [
        StringCalculator(check_empty_input, return_zero_for_empty_input),
        StringCalculator(check_for_custom_delimiter_and_replace_with_comma, sum_numbers),
        StringCalculator(check_newline_delimiter_and_replace_with_comma, sum_numbers),
        StringCalculator(check_for_negative_input, print_exception_if_negative_number),
    ]

    return_value = 0

    for calculator in calculators:
        calculator.enabled = calculator.check_function(numbers)
        if calculator.enabled:
            if calculator.result_function == sum_numbers:
                return_value = calculator.result_function(modified_numbers)
            else:
                calculator.result_function(modified_numbers)
            break

    return_value = return_sum_if_default_delimiter(numbers, return_value)

    return return_value
