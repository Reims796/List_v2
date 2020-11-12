def ft_len(a):
    b = 0
    for i in a:
        a += 1
    return a


def ft_odd_even_separator_lst(lst):
    a = 0
    for i in lst:
        a = a + 1
    b = a
    i = 0
    n = []
    k = []
    x = [[0], [0]]
    for i in range(b):
        if lst[i] % 2 == 0:
            n.append(lst[i])
        elif lst[i] % 2 != 0:
            k.append(lst[i])
        i += 1
    x[0] = n
    x[1] = k
    return x
