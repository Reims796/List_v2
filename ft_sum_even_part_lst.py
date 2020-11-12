def ft_sum_even_part_lst(lst):
    a = 0
    for i in lst:
        a += 1
    i = 0
    b = a
    x = 0
    for i in range(b):
        if lst[i] % 2 == 0:
            x += lst[i]
        i += 1
    return x
