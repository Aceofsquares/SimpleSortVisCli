from random import randint

def radixsort(arr):
    max_digits = maxdigits(arr)
    print(f"Maximum number of digits in array: {max_digits}")
    buckets = [[] for _ in range(10)]

    mod = 10
    div = 1
    for _ in range(max_digits):
        while len(arr) > 0:
            num = arr.pop(0)
            loc = (num // div) % 10
            print(f"Num: {num} | Loc: {loc} | Mod: {mod} | Div: {div}")
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
    maxsize = 0
    for i in arr:
        size = 0
        while i != 0:
            size += 1
            i = i // 10
        if size > maxsize:
            maxsize = size
    return maxsize
