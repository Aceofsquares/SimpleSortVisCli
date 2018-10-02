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
    merged += arr1[idx1:]
    merged += arr2[idx2:]
    print(merged)
    print(f"Merged {merged}", end="\n\n")
    return merged

