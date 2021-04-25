def extend_result(res, source, it):
    while True:
        try:
            res.append(next(it))
        except StopIteration:
            break


def merge(list_a, list_b):
    list_res = []

    it_a = iter(list_a)
    it_b = iter(list_b)
    a, b = next(it_a), next(it_b)
    while True:
        list_res.append(min(a, b))
        if a > b:
            try:
                b = next(it_b)
            except StopIteration:
                list_res.append(a)
                extend_result(list_res, list_a, it_a)
                break
        else:
            try:
                a = next(it_a)
            except StopIteration:
                list_res.append(b)
                extend_result(list_res, list_b, it_b)
                break
    if isinstance(list_a, list):
        return list_res
    else:
        return tuple(list_res)
