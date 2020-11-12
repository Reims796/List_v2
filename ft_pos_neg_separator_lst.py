def ft_len(a):
    b = 0
    for i in a:
        a += 1
    return a


def ft_pos_neg_separator_lst(lst):
    a = 0
    for i in lst:
        a += 1
    b = a
    i = 0
    c = []
    e = []
    d = []
    x = [[0], [0], [0]]
    for i in range(b):
        if lst[i] > 0:
            c.append(lst[i])
        elif lst[i] < 0:
            e.append(lst[i])
        else:
            d.append(lst[i])
        i = i + 1
    x[0] = e
    x[1] = d
    x[2] = c
    return x
