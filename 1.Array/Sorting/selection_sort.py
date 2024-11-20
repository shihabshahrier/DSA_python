import random as rand

def selectionSort(arr):
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [rand.randint(1,100) for _ in range(10)]
    print("previously: ", arr)
    selectionSort(arr)
    print("After Sorting: ", arr)