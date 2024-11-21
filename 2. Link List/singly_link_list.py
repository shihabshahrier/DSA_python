class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
class SinglyLinkList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        self.size = 0
    
    def isEmpty(self):
        return self.head is None
    
    def addNodeLast(self, val):
        n = Node(val)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail = self.tail.next
        self.size += 1

    def addNodeFirst(self, val):
        n = Node(val)
        if self.isEmpty():
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n
        self.size += 1

    def removeNode(self, val:any)->None:
        if val == self.head.val:
            self.head = self.head.next
            self.size -= 1
            return
        
        n = self.head
        while n.next:
            if n.next.val == val:
                if n.next == self.tail:
                    n.next = None
                    self.tail = n
                    return
                n.next = n.next.next
                self.size -= 1
                return
            n = n.next
        
    def printLinkList(self):
        n = self.head
        while n:
            if not n.next:
                print(f"{n.val}")
            else:
                print(f"{n.val} -> ", end = "")
            n = n.next

    def __iter__(self):
        n = self.head
        while n:
            yield n.val
            n = n.next

    def __str__(self):
        return " -> ".join(map(str, self)) if not self.isEmpty() else "Empty List"

    
        

if __name__ == "__main__":
    nums = [i for i in range(10)]
    ll = SinglyLinkList()
    for i in nums[:5]:
        ll.addNodeLast(i)
    ll.printLinkList()
    for i in nums[5:]:
        ll.addNodeFirst(i)
    ll.printLinkList()
    print(ll.head.val)
    ll.removeNode(4)
    print(ll)
  
         