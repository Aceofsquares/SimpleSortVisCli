def quicksort(arr):
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
    sorted_less = quicksort(less_than)
    print(f"{sorted_less} + pivot({equal_to}): \n\t{sorted_less + equal_to}")
    sorted_less += equal_to
    print(f"Greater than {pivot}: \n\t{greater_than}")
    sorted_greater = quicksort(greater_than)
    print(f"sorted_less({sorted_less}) + sorted_greater({sorted_greater}): \n\t", end='')
    print(sorted_less + sorted_greater, end="\n\n")
    return sorted_less + sorted_greater


def median(arr):
    f = arr[0]
    s = arr[len(arr)//2]
    t = arr[len(arr)-1]
    return max(min(f, s), min(max(f, s), t))