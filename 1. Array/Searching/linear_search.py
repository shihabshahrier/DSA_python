import random as rand

def linearSearch(arr, val):
    for i in arr:
        if i == val:
            return True
    return False

if __name__ == "__main__":
    arr = [rand.randint(1,100) for _ in range(10)]
    print(arr)
    val = 10
    x = linearSearch(arr, val)
    print(f"{val} is in Array:", x)