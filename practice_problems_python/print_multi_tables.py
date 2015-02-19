# print 12x12 multipcation table


def multiTable(n):
    for x in xrange(1, n):
        for y in xrange(1, n):
            print x * y, '\t',
        print

multiTable(12)
