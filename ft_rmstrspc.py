def ft_rmstrspc(str):
    a = 0
    for i in str:
        a = a + 1
    b = a
    x = ''
    i = 0
    for i in range(b):
        if str[i] == ' ':
            i += 1
        else:
            x += str[i]
            i += 1
    return x
