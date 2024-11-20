import random as rand

def pertition(arr, l, r):
    pivot = arr[r]
    j = l-1
    for i in range(l, r):
        if arr[i] <= pivot:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
            
    arr[j+1], arr[r] = arr[r], arr[j+1]
    return j+1

def quickSort(arr, l, r):
    if l < r:
        pivot = pertition(arr, l, r)
        quickSort(arr, l, pivot-1)
        quickSort(arr, pivot+1, r)

if __name__ == "__main__":
    arr = [rand.randint(1,100) for _ in range(10)]
    print("previously: ", arr)
    quickSort(arr, 0, len(arr)-1)
    print("After Sorting: ", arr)