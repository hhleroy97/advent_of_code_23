from functools import reduce


def calc_min_cubes(input_string):
    subset_array = input_string.split(':')[1].strip().split(';')

    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for set in subset_array:
        set = set.split(',')
        for pair in set:
            pair = pair.strip().split(' ')
            if int(pair[0]) > min_cubes.get(pair[1]):
                min_cubes[pair[1]] = int(pair[0])

    return reduce(lambda x, y: x * y, min_cubes.values())

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_lines = open('input.txt', 'r').readlines()

    sum = 0

    for line in file_lines:
        sum += calc_min_cubes(line)

    print(sum)