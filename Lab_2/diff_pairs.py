def get_pairs_count(num_list, m):
    dict_num = {}
    count = 0
    for a in num_list:
        if a not in dict_num:
            dict_num[a] = False
        elif not dict_num[a]:
            count += 1
            dict_num[a] = True
    if not m:
        return count
    count = 0
    for a in dict_num:
        if a + m in dict_num:
            count += 1
    return count
