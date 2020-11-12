def ft_join(lst, n=' '):
    z = 0
    for i in lst:
        z += 1
    i = 0
    x = ''
    for i in range(z):
        x += lst[i]
        if i != d - 1:
            x += n
        i += 1
    return x
