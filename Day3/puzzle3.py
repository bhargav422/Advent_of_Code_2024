import re
import copy
def uncorrupted_mul(file):
    """
    Reads a file, removes specific patterns, and finds multiplication expressions.
    Args:
        file (str): The path to the file to be read.
    Returns:
        list: A list of strings, each representing a multiplication expression found in the file.
    The function performs the following steps:
    1. Reads the content of the specified file.
    2. Removes all occurrences of the pattern "don't()(.*?)do()" from the file content.
    3. Finds all occurrences of the pattern 'mul(d{1,3},d{1,3})' in the modified content.
    4. Returns a list of these found multiplication expressions.
    """
    
    find_dont = "don't()(.*?)do()"
    with open(file) as fr:
        reader = fr.read()

    x = re.sub(find_dont, '', reader)

    print(x)
    find_mul = r'mul\(\d{1,3},\d{1,3}\)'
    mullify = re.findall(find_mul, x)

    return mullify

def muliply_data(mul_list):
    """
    Multiplies pairs of integers found in strings within a list and returns the sum of the products.

    Args:
        mul_list (list of str): A list of strings, each containing two integers.

    Returns:
        int: The sum of the products of the pairs of integers found in the input list.

    Example:
        >>> muliply_data(["3 4", "2 5"])
        23
    """
    int_data = r"\d+"
    multiples = []
    for ele in mul_list:
        num = re.findall(int_data, ele)
        mul_n = int(num[0]) * int(num[1])
        multiples.append(mul_n)

    return sum(multiples)

def part_two(file):
    """
    Processes a file containing specific patterns and calculates a sum based on the patterns found.

    The function reads the content of the given file and searches for patterns using regular expressions.
    The patterns include 'do()', 'don't()', and 'mul(x,y)' where x and y are integers.
    - 'do()' sets a flag to True, allowing multiplication results to be added to the sum.
    - 'don't()' sets the flag to False, preventing multiplication results from being added to the sum.
    - 'mul(x,y)' multiplies x and y, and if the flag is True, the result is added to the sum.

    Args:
        file (str): The path to the file to be processed.

    Returns:
        int: The sum of the multiplication results based on the patterns and the flag state.
    """
    do_sum = True
    sum_mul = 0
    with open(file) as fr:
        reader = fr.read()
    do_dont_pattern = r'do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\)'
    for x in re.finditer(do_dont_pattern, reader):
        match x[0]:
            case 'do()':
                do_sum = True
            case 'don\'t()':
                do_sum = False
            case _:
                if do_sum:
                    sum_mul += int(x[1]) * int(x[2])
    return sum_mul

if __name__ == '__main__':
    mul_list = uncorrupted_mul('input_data.txt')
    # mul_list = uncorrupted_mul('demo_data.txt')
    sum_of_mul = muliply_data(mul_list)
    redefined_mul = part_two('input_data.txt')
    print(redefined_mul)