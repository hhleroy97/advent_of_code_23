import re


def extract_number_from_line(input_string):

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
        sum += extract_number_from_line(line)

    print(sum)