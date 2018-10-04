from random import randint
from functools import reduce

'''
Doesn't work with negative values...yet.
'''
def radixsort(arr):
    buckets = [[] for _ in range(10)]

    div = 1
    tmp = None
    cont = True
    # for i in range(max_digits):
    while cont:
        idx = 0
        tmp = [v for v in arr]
        cont2 = False
        while len(arr) > 0:
            num = arr.pop(0)
            loc = (num // div) % 10
            if (num // div) > 0:
                cont2 = True
            tmp2 = [f"*{val}*" if i == idx else f"{val}" for (i, val) in enumerate(tmp)]
            idx += 1
            print(f"Array: {'[ ' + ' | '.join(tmp2) + ' ]'}")
            print(f"Num: {num} | Div: {div} | Loc ({num}//{div}) % 10: {loc}")
            buckets[loc].append(num)
            print_buckets(buckets, loc, num)
        for bucket in buckets:
            if bucket:
                while len(bucket) > 0:
                    arr.append(bucket.pop(0))
        div *= 10
        print(f"Result Array: {arr}\n")
        cont = cont2
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