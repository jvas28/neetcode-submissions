class Node:
    next : Node | None = None
    
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def setValue(self, value:int):
        self.value = value

    def append(self, node):
        self.next = node
    

class LinkedList:
    head : Node | None = None

    def __init__(self):
        self.head = None
    
    def get(self, index: int) -> int:
        if(self.head is None):
            return -1

        current = self.head
        if(index > 0):
            for i in range(1, index + 1):
                current = current.next
                if current is None:
                    break
                if index == i:
                    return current.value
        else:
            if current is not None:
                return current.value
        
        return -1
        

    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        self.head = new_head
        

    def insertTail(self, val: int) -> None:
        if(self.head is None):
            self.head = Node(val)
            return

        current = self.head
        while current.next is not None:
            current = current.next
        
        current.next = Node(val)
        

    def remove(self, index: int) -> bool:
        if self.head is None:
            return False

        current = self.head
        if index > 0:
            for i in range(1, index):
                if current.next is None:
                    break
                current = current.next
            if(current.next is not None):
                toRemove = current.next
                current.next = toRemove.next
                return True
        else: 
            next = current.next
            self.head = next
            return True
        return False
      

    def getValues(self) -> List[int]:
        if self.head is None:
            return []

        current = self.head
        values = [current.value]
        
        while current.next is not None:
            current = current.next
            values.append(current.value)
        return values

