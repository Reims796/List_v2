def ft_sum_even_lst(lst):
    a = 0
    for i in lst:
        a = a + 1
    b = a
    i = 0
    x = 0
    for i in range(b):
        if i % 2 == 0:
            x += lst[i]
        i += 1
    return x
