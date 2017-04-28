
import itertools
def product(num):
    nn = str(num)
    max = 1
    for t in list(itertools.permutations(nn,len(nn))):
        n = "".join(t)
        i = 1
        while i < len(n):
            p = int(n[0:i]) * int(n[i:])
            if max < p:
                max = p
            i += 1
    return max

print(product(123456))