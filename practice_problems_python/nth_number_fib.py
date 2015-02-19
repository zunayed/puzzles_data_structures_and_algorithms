#find the nth number of a fibanaci sequence


def fib(number):
    if number <= 1:
        return number
    else:
        return (fib(number - 1) + fib(number - 2))


for num in xrange(1, 10):
    print fib(num)
