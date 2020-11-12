def ft_join(lst, sep=' '):
    a = 0
    for i in lst:
        a += 1
    b = a
    x = ''
    i = 0
    for i in range(b):
        x += lst[i]
        if i != b - 1:
            x += sep
        i += 1
    return x
