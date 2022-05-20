
def gcd(a: int, b: int):
    if a == 0:
        return b
    return gcd(b%a, a)

def lcm(a: int, b: int):
    return (a*b)//gcd(a, b)

def create_pairs(n, array):
    for i in range(n):
        for j in range(i+1, n):
            yield lcm(array[i], array[j])

def orak_lcm(n: int, array):

    # pair_lcm = list()
    # for i, x in enumerate(array):
    #     for j, y in enumerate(array[i+1:]):
    #         pair_lcm.append(lcm(x, y))

    pair_gen = create_pairs(n, array)
    _gcd = 0
    for i in pair_gen:
        cur_gcd = gcd(i, next(pair_gen, 0))
        _gcd = gcd(_gcd, cur_gcd)
    return _gcd

print(orak_lcm(4, [10, 24, 40, 80]))``
print(orak_lcm(10, [540, 648, 810, 648, 720, 540, 594, 864, 972, 648]))

n = int(input())
array = list(map(int, input().split()))
print(orak_lcm(n, array))
