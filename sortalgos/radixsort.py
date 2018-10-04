from random import randint
from functools import reduce

'''
Doesn't work with negative values...yet.
'''
def radixsort(arr):
    max_digits = maxdigits(arr)
    print(f"Maximum number of digits in array: {max_digits}\n")
    buckets = [[] for _ in range(10)]

    div = 1
    tmp = None
    for i in range(max_digits):
        idx = 0
        tmp = [v for v in arr]
        while len(arr) > 0:
            num = arr.pop(0)
            loc = (num // div) % 10
            tmp2 = [f"*{val}*" if i == idx else f"{val}" for (i, val) in enumerate(tmp)]
            idx += 1
            print(f"Array: {'[ ' + ' | '.join(tmp2) + ' ]'}")
            print(f"Num: {num} | Loc: {loc} | Div: {div}")
            buckets[loc].append(num)
            print_buckets(buckets, loc, num)
        for bucket in buckets:
            if bucket:
                while len(bucket) > 0:
                    arr.append(bucket.pop(0))
        div *= 10
        print(f"Result Array: {arr}\n")
    return arr

def print_buckets(buckets, loc, num):
    bucket_num = 0
    for bucket in buckets:
        print(f"{bucket_num}: {bucket}", end="")
        if loc == bucket_num:
            print(f" <-- Placement")
        else:
            print()
        bucket_num += 1
    print()

def maxdigits(arr):
    maxvalue = reduce(lambda x,y: x if x > y else y, arr)
    maxsize = 0
    while maxvalue > 0:
        maxsize += 1
        maxvalue //= 10
    return maxsize