import re

digit_mapping = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

def replace_spelled_digits(input_string):
    result = ''

    i = 0

    while i < len(input_string):
        found_digit = False

        for digit in sorted(digit_mapping.keys(), key=len, reverse=True):
            if input_string[i:].startswith(digit):
                result += digit_mapping[digit]
                i += 1
                found_digit = True
        if not found_digit and input_string[i].isdigit():
            result += input_string[i]
            i += 1
        elif not found_digit:
            i += 1

    return result

def extract_number(input_string):
    extracted_numbers = [digit for digit in re.findall(r'\d', input_string)]

    if len(extracted_numbers) == 1:
        return int("".join([extracted_numbers[0],extracted_numbers[0]]))
    else:
        return int("".join([extracted_numbers[0],extracted_numbers[-1]]))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_lines = open('input.txt', 'r').readlines()

    sum = 0

    for line in file_lines:
        sum += extract_number(replace_spelled_digits(line.strip()))

    print(sum)