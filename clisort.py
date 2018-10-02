from random import randint, choice
from argparse import ArgumentParser
from sys import exit

def median(arr):
    f = arr[0]
    s = arr[len(arr)//2]
    t = arr[len(arr)-1]
    return max(min(f, s), min(max(f, s), t))

def qsort(arr):
    if len(arr) <= 1:
        return arr
    temp = [v for v in arr]
    pivot = median(temp)
    temp.remove(pivot)

    less_than = []
    greater_than = []
    equal_to = [pivot]
    for e in temp:
        if e < pivot:
            less_than.append(e)
        elif e > pivot:
            greater_than.append(e)
        else:
            equal_to.append(e)

    print(f"Pivot: {pivot}\n")
    print(f"Less than {pivot}: \n\t{less_than}")
    sorted_less = qsort(less_than)
    print(f"{sorted_less} + pivot({equal_to}): \n\t{sorted_less + equal_to}")
    sorted_less += equal_to
    print(f"Greater than {pivot}: \n\t{greater_than}")
    sorted_greater = qsort(greater_than)
    print(f"sorted_less({sorted_less}) + sorted_greater({sorted_greater}): \n\t", end='')
    print(sorted_less + sorted_greater, end="\n\n")
    return sorted_less + sorted_greater
    
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    bot = arr[:len(arr)//2]
    top = arr[len(arr)//2:]

    print(f"Split\t{arr} \n\t{bot} -||- {top}", end="\n\n")
    bot = mergesort(bot)
    top = mergesort(top)

    return merge(bot, top)

def merge(arr1, arr2):
    merged = []
    idx1 = 0
    idx2 = 0
    print(f"{arr1} merge with {arr2}")
    while idx1 < len(arr1) and idx2 < len(arr2):
        if idx2 < len(arr2) and arr1[idx1] <= arr2[idx2]:
            merged.append(arr1[idx1])
            idx1 += 1
            print(merged)
        if idx1 < len(arr1) and arr2[idx2] < arr1[idx1]:
            merged.append(arr2[idx2])
            idx2 += 1
            print(merged)
    while idx1 < len(arr1):
        merged.append(arr1[idx1])
        idx1 += 1
    while idx2 < len(arr2):
        merged.append(arr2[idx2])
        idx2 += 1
    print(merged)
    print(f"Merged {merged}", end="\n\n")
    return merged

def insertion(arr):
    if len(arr) <= 1:
        return arr
    i = 0
    while i < len(arr) - 1:
        j = i + 1
        print(f"Placing {arr[j]}")
        while j > 0:
            print(f"is {arr[j-1]} > {arr[j]} -> {'yes' if arr[j-1] > arr[j] else 'no'}")
            if arr[j-1] > arr[j]:
                print(f"Swap them")
                temp = arr[j]
                arr[j] = arr[j - 1]
                arr[j - 1] = temp
            else:
                break
            print(arr)
            j -= 1
        print(f"Done for {arr[j]}\n")
        i += 1
    
    return arr
            
def selection(arr):
    if len(arr) <= 1:
        return arr
    for i in range(len(arr)-1):
        print(f"Smallest element of {arr[i:]}")
        for j in range(i+1, len(arr)):
            print(f"is {arr[j]} < {arr[i]} -> {'yes' if arr[j] < arr[i] else 'no'}")
            if(arr[i] > arr[j]):
                temp = arr[i]
                arr[i] = arr[j]
                arr[j] = temp
                print(f"Swapped: {arr[i:]}")
        print(f"smallest -> {arr[i]}")
        print(arr, end="\n\n")

    return arr

parser = ArgumentParser()

parser.add_argument('amount', type=int, help="Amount of integers in list")
parser.add_argument('-s', '--sortmode', nargs=1, type=str, help="Sort mode. Default: Neither.  Options: quick, merge")
parser.add_argument('-m', '--min', type=int, default=0, help="Minimum value of an integer. Default: 0")
parser.add_argument('-x', '--max', type=int, default=1000, help="Maximum value of an integer. Default: 1000")

args = parser.parse_args()

if args.amount <= 0:
    print("Amount of integers must be greater than 0")
    exit(1)

if args.min > args.max:
    print("Minimum must be greater than maximum")
    exit(2)

values = [randint(args.min, args.max) for _ in range(args.amount)]

sorted_list = []
print(f"\nUnsorted values: {', '.join(map(str, values))}\n")
if args.sortmode:
    if args.sortmode[0] in ("quick", "qui"):
        sorted_list = qsort(values)
    elif args.sortmode[0] in ("merge", "mer"):
        sorted_list = mergesort(values)
    elif args.sortmode[0] in ("insertion", "ins"):
        sorted_list = insertion(values)
    elif args.sortmode[0] in ("selection", "sel"):
        sorted_list = selection(values)
else:
    sorted_list = sorted(values)

print(f"Sorted values: {', '.join(map(str, sorted_list))}\n")
