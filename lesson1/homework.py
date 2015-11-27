l = [0, 1, 2, 3, 4, 5]
x = 0

if len(l) == 0:
    x = 0
else:
    for n in l:
        if l.index(n) % 2 != 0:
            x += n
    x = x * l[-1]

print x