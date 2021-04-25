def get_subarrays_count(array, m):
    list_len = len(array)
    num = 0
    for start_index in range(list_len):
        num_sum = 0
        for i in range(start_index, list_len):
            num_sum += array[i]
            if num_sum == m:
                num += 1
    return num
