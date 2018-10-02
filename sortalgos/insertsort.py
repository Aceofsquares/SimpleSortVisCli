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