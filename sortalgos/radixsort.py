from random import randint
from functools import reduce

'''
Doesn't work with negative values...yet.
'''
def radixsort(arr):
    max_digits = maxdigits(arr)
    print(f"Maximum number of digits in array: {max_digits}\n")
    buckets = [[] for _ in range(10)]

    mod = 10
    div = 1
    for _ in range(max_digits):
        while len(arr) > 0:
            num = arr.pop(0)
            loc = (num // div) % 10
            print(f"Num: {num} | Loc: {loc} | Div: {div} | Mod: {mod} ")
            buckets[loc].append(num)
            print(buckets, end="\n\n")
        for bucket in buckets:
            if bucket:
                while len(bucket) > 0:
                    arr.append(bucket.pop(0))
        mod *= 10
        div *= 10
    return arr
            

def maxdigits(arr):
    maxvalue = reduce(lambda x,y: x if x > y else y, arr)
    maxsize = 0
    while maxvalue > 0:
        maxsize += 1
        maxvalue //= 10
    return maxsize