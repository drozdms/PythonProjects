from beauty import get_beauties
from subarrays import get_subarrays_count
from merge import merge
from card_number import check_card_number
from card_number import check_card_number_str
from card_number import generate_card_number

# coding=utf-8


if __name__ == '__main__':
    # print(get_beauties(61))
    # print(get_subarrays_count([1, 0, 1, 1], 2))
    #
    # print(get_subarrays_count([2, 0, -2, 2], 0))
    # print(merge([1, 2, 7], [3, 9, 12, 19]))
    # print(merge((3, 15), (7, 8)))
    n = generate_card_number("Visa")
    print(n)
    print(check_card_number(n))
    # num = [1, 2, 3, 7, 9]
    # print(sum(num[1:]))
    # print(sum(num))
    # print(sum(num[:len(num)-1]))
    print(check_card_number(5082337440657324))
    print(check_card_number_str("5082337440657324"))