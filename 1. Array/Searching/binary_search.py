import random as rand

def binarySearch(arr, val):
    l = 0
    r = len(arr) - 1

    while l <= r:
        mid = (l + r)//2
        if arr[mid] == val:
            return True
        elif val > arr[mid]:
            l = mid + 1
        elif val < arr[mid]:
            r = mid - 1
    return False

def reBinarySearch(arr, val, l, r):
    if l > r:
        return False
    mid = (l+r)//2
    if arr[mid] == val:
        return True
    elif val > arr[mid]:
        return reBinarySearch(arr, val, mid+1, r)
    elif val < arr[mid]:
        return reBinarySearch(arr, val, l, mid - 1)


if __name__ == "__main__":
    arr = [ _ for _ in range(10)]
    print(arr)
    val = 5
    # x = binarySearch(arr, val)
    x = reBinarySearch(arr, val, 0, len(arr)-1)
    print(f"{val} is in Array:", x)
