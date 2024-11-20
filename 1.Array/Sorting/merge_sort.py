import random as rand

def merge(arr1, arr2):
    result = []
    i, j = 0, 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    result += arr1[i:]
    result += arr2[j:]
    return result

def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    a = mergeSort(arr[:mid])
    b = mergeSort(arr[mid:])
    return merge(a, b)


if __name__ == "__main__":
    arr = [rand.randint(1,100) for _ in range(10)]
    print("previously: ", arr)
    x = mergeSort(arr)
    print("After Sorting: ", x)