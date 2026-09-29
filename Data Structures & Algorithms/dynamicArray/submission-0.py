class DynamicArray:

    
    def __init__(self, capacity: int):
        self.myList = [0] * capacity
        self.capacity = capacity
        self.size = 0;


    def get(self, i: int) -> int:
        return self.myList[i]


    def set(self, i: int, n: int) -> None:
        self.myList[i] = n

    def pushback(self, n: int) -> None:
        if(self.size == self.capacity):
            self.resize()
        self.myList[self.size] = n
        self.size += 1
        


    def popback(self) -> int:
        self.size -= 1
        return self.myList[self.size];

    def resize(self) -> None:
        self.capacity = self.capacity * 2;
        new_arr = [0] * self.capacity
        for i in range(self.size):
            new_arr[i] = self.myList[i]
        self.myList = new_arr
        


    def getSize(self) -> int:
        return self.size
        
    
    def getCapacity(self) -> int:
        return self.capacity
