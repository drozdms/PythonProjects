def transpose(double_iterable_object):
    return zip(*double_iterable_object)


def return_number_or_error(a):
    return int(a) if isinstance(a, str) else a


def scalar_product(iterable_1, iterable_2):
    try:
        return sum(map(lambda a, b: return_number_or_error(a) * return_number_or_error(b), iterable_1, iterable_2))
    except ValueError:
        return None
