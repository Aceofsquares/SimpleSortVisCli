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