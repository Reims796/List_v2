def ft_rmstrchar(str, less):
    a = 0
    for i in str:
        a += 1
    b = a
    a = 0
    for i in less:
        a += 1
    i = 0
    z = 0
    c = a
    x = ''
    while b > i and c > z:
        if str[i] == less[z]:
            i = i + 1
            z = 0
        elif str[i] != less[z] and z == c - 1:
            x += str[i]
            i += 1
            z = 0
        else:
            z += 1
    return x
