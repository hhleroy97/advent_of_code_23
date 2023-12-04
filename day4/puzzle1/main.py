def calculate_card_value(input_string):
    card = input_string.strip().split(':')[1].split('|')

    winning_nums = card[0].strip().split(' ')
    winning_nums = [int(x) for x in winning_nums if x != '']

    card_nums = card[1].strip().split(' ')
    card_nums = [int(x) for x in card_nums if x != '']

    match_count = 0

    for num in card_nums:
        if num in winning_nums:
            match_count += 1

    if match_count < 1:
        score = 0
    else:
        score = 2**(match_count-1)

    return score


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    file_lines = open('input.txt', 'r').readlines()

    sum = 0

    for line in file_lines:
        sum += calculate_card_value(line)

    print(sum)
