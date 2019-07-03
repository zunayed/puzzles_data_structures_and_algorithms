
# Complete the function below.
def gen_subsets(s, seen, index, output):
    if index == len(s):
        return [''.join(seen)]

    l = gen_subsets(s, seen, index+1, output)
    seen = seen + [s[index]]
    r = gen_subsets(s, seen, index+1, output)

    return l + r

def generate_all_subsets(s):
    return gen_subsets(s, [], 0, [])

output = generate_all_subsets("xy")
for x in output:
    print(x)
