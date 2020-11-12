def ft_len(a):
    b = 0
    for i in a:
        a += 1
    return a


def ft_join(n, b):
    x = ""
    z = 0
    if not b:
        b = " "
    while z != ft_len(n) - 1:
        x = x + n[z] + b
    x += n[-1]
    return x
