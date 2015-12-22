print "Task for 'if-else':\n"

n1 = 3
n2 = 5
n3 = 8

if n1 > n2 and n1 > n3:
    if n2 > n3:
        nn = n1 + n2
    else:
        nn = n1 + n3
elif n2 > n3 and n2 > n1:
    if n1 > n3:
        nn = n2 + n1
    else:
        nn = n2 + n3
elif n2 > n1:
    nn = n3 + n2
else:
    nn = n3 + n1

print 'Max two numbers sum = %s' % (nn)

print "\n\nTask for 'for':\n"

price = 10.25
kg = 10

for n in range(1, kg + 1):
    print 'Price for %s kg = %s' % (n, n * price)

print "\n\nTask for 'while':\n"

kg2 = 2
n2 = 1.2

while n2 <= kg2:
    print 'Price for %s kg = %s' % (n2, n2 * price)
    n2 += 0.2

print "\n\nTask for 'break':\n"

br = [32143, -13, 0, 10, 20, 42, 60, 100]

for n3 in br:
    if n3 == 42:
        print "The Answer to the Ultimate Question of Life, the Universe, and Everything"
        break
    if len(str(abs(n3))) < 3:
        print 'Numbers count less than 3: %s' % (n3)

print "\n\nTask for 'continue':\n"

cn = [15, 20, 26, 39, 10]

for n4 in cn:
    if n4 % 13 != 0:
        continue
    else:
        print 'Divides by 13: %s' % (n4)
