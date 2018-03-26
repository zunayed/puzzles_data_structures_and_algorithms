# Problem 1
# We can do this faster with a variety of algos accoring to wiki
# https://en.wikipedia.org/wiki/Primality_test

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True

    if n % 2 == 0:
        return False

    # skip even numbers
    for i in range(3, n, 2):
        if n % i == 0:
            return False

    return True

def prime_numbers(num_to_print):
    count = 0
    cur_num = 0

    while count < num_to_print:
        if is_prime(cur_num):
            yield cur_num
            count += 1

        cur_num += 1


# simple tests
for num_to_test in [2, 3, 5, 7, 181]:
    assert is_prime(num_to_test) == True

for num_to_test in [-1, 0, 1, 9, 12, 200, 3400]:
    assert is_prime(num_to_test) == False

print list(prime_numbers(10))
assert len(list(prime_numbers(10))) == 10

# Problem 2
"""
    // Problem 2
    Vector<Integer> inter1 = new Vector<Integer>();
    inter1.add(1);
    inter1.add(2);
    inter1.add(3);
    inter1.add(25);
    Vector<Integer> inter2 = new Vector<Integer>();
    inter2.add(2);
    inter2.add(3);
    inter2.add(15);
    inter2.add(25);

"""

# Assuming you want the unique intersection items
# solution 1
def intersection1(a1, a2):
    s1 = set(a1)
    s2 = set(a2)

    return sorted(s1.intersection(s2))

# solution 2
# return all common values
def intersection2(a1, a2):
    return [x for x in a1 if x in a2]

assert intersection1([1,2,2,3,25], [2,3,15,25]) == [2,3,25]
assert intersection2 ([1,2,2,3,25], [2,3,15,25]) == [2,2,3,25]

print intersection1([1,2,2,3,25], [2,3,15,25])
print intersection2([1,2,2,3,25], [2,3,15,25])

# Problem 3
"""
(1) split on newline
(2) split on ,
(3) strip quotes
"""
def parse_csv(input):
    output = []
    lines = input.split("\n")
    for l in lines:
        row_to_add = []
        for item in l.split(","):
            row_to_add.append(item.replace('"', ""))

        output.append(row_to_add)

    return output

sample_input = "1514764800,US,United States,15,\"$1,500\"\n1514764800,CA,Canada,2,$200\n"
print parse_csv(sample_input)
