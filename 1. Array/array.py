class Array:
    def __init__(self, lenght):
        self.arr = [float("-inf") for _ in range(lenght)]
        self.lenght = lenght
        self.size = 0
    
    def insert(self, ind, val):
        if -1 <= ind >= self.lenght:
            raise "out of index"
        self.arr[ind] = val
        self.size += 1
    def remove(self, ind):
        if -1 <= ind >= self.lenght:
            raise "out of index"
        self.arr[ind] = float("-inf")
        self.size -= 1

    def get(self, ind):
        if -1 <= ind >= self.lenght:
            raise "out of index"
        return self.arr[ind]
    
    def lenght(self):
        return self.size
    
    def __str__(self):
        return str(self.arr)
    
if __name__ == "__main__":
    arr = Array(10)
    print(arr)