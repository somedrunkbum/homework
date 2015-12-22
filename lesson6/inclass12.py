D = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 0: 'zero'}
res = []


def foo(num):
    for i in str(num):
        for l in D:
            if i == str(l):
                res.append(D[l])
    return ' '.join(res)


print foo(5214)
