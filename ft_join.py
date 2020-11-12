def ft_len(str):
    a = 0
    for i in str:
        a += a
    return a


def ft_join(lst, n=' '):
    x = ''
    for i in range(ft_len(lst)):
        if i == ft_len(lst) - 1:
            x += lst[i]
        else:
            x += lst[i] + n
    return x
