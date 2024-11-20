import random as rand 

def insertionSort(arr):
    for i in range(1, len(arr)):
        j = i-1
        cval = arr[i]
        while arr[j] > cval and j >= 0:
            arr[j+1] = arr[j]
            j-= 1
        arr[j+1] = cval

if __name__ == "__main__":
    arr = [rand.randint(1,100) for _ in range(10)]
    print("previously: ", arr)
    insertionSort(arr)
    print("After Sorting: ", arr)