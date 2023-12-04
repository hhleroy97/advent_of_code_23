def add_character_to_lines(input_string, character):
    # Split the input string into lines
    lines = input_string.split('\n')

    # Add the character to the start and end of each line
    lines_with_character = [character + line + character for line in lines]

    # Join the lines back into a single string
    result = '\n'.join(lines_with_character)

    return result

def is_symbol(char):
    return char in {'*', '+', '%', '@', '$', '=', '&', '#', '/', '-'}

def sum_part_numbers(engine):
    total_sum = 0

    row = 1
    col = 1

    while row < len(engine)-1:
        while col < len(engine[row])-1:
            num = ''

            i = 0
            while engine[row][col + i].isdigit():
                num = num + engine[row][col + i]
                i += 1

            symbol_adjacent = False

            if num.isdigit():
                j = -1
                while j <= 1:
                    k = -1
                    while k <= len(num):
                        if is_symbol(engine[row+j][col+k]):
                            symbol_adjacent = True
                            total_sum += int(num)

                        k += 1
                    j += 1

            if len(num) > 1:
                col += len(num)
            else:
                col += 1


        col = 0
        row += 1

    return total_sum

if __name__ == '__main__':
    file_path = 'input.txt'
    with open(file_path, 'r') as file:
        engine_schematic = file.read()

    # Convert the string into a list of strings (each string representing a row)
    engine_schematic = engine_schematic.split('\n')

    hold = ['x'*len(engine_schematic[0])]
    for line in engine_schematic:
        hold.append(add_character_to_lines(line,'x'))
    hold.append('x'*len(engine_schematic[0]))

    engine_schematic = hold

    # Calculate the sum of part numbers
    result = sum_part_numbers(engine_schematic)

    print(result)