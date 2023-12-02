constraints = {
    'red' : 12,
    'green' : 13,
    'blue' : 14
}


def is_possible(input_string):
    subset_array = input_string.split(':')[1].strip().split(';')

    for set in subset_array:
        set = set.split(',')
        for pair in set:
            pair = pair.strip().split(' ')
            if int(pair[0]) > constraints.get(pair[1]):
                return False

    return True

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_lines = open('input.txt', 'r').readlines()

    game_num = 1
    sum = 0

    for line in file_lines:
        if is_possible(line):
            sum += game_num

        game_num += 1

    print(sum)