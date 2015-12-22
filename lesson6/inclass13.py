l = (2, 3, 4, 5)
m = []


def foo(tup):
    for i in tup:
        if i % 2 == 0:
            m.append(i)
    return tuple(m)


print foo(l)