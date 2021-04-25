def distribute(num_list, m):
    max_num = max(num_list)
    min_num = min(num_list)
    seg_len = (max_num - min_num) / m
    segments = [0] * (m + 1)

    for a in num_list:
        segments[int((a - min_num)/seg_len)] += 1

    segments[m - 1] += segments.pop(m)
    return segments
