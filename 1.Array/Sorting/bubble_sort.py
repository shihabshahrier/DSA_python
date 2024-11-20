import random as rand

def bubbleSort(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

if __name__ == "__main__":
    arr = [rand.randint(1,100) for _ in range(10)]
    print("previously: ", arr)
    bubbleSort(arr)
    print("After Sorting: ", arr)