import random


def get_modified_card_sum(num):

    for i in range(1, len(num), 2):
        num[i] = 2 * num[i]
        if num[i] > 9:
            num[i] = num[i] - 9
    return sum(num)


def build_array_from_number(card_number):
    num = []
    while card_number >= 1:
        card_number, r = divmod(card_number, 10)
        num.append(r)
    return num


def generate_card_number(card_type):
    random.seed()
    card_num = 0
    card_num += random.randint(0, 10**15 - 1)
    print(card_num)
    card_num += 4*1e15 if card_type == "Visa" else 5*1e15
    print(card_num)
    check_digit = card_num % 10 + (10 - get_modified_card_sum(build_array_from_number(card_num)) % 10)
    return card_num - card_num % 10 + (check_digit if check_digit <= 9 else check_digit - 10)


def check_card_number(card_number):
    return not get_modified_card_sum(build_array_from_number(card_number)) % 10


def check_card_number_str(card_number):
    return not get_modified_card_sum([ord(number_char) - 48 for number_char in card_number[::-1]]) % 10
