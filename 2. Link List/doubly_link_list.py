class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
    
class DoublyLinkList:
    def __init__(self, head = None):
        self.head = head
        self.tail = head
        
    def addNodeLast(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            self.tail.next = n
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

    def addNodeFirst(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head.prev = n
            self.head = n

    def printLinkList(self):
        n = self.head
        while n:
            if not n.next:
                print(f"{n.val}")
            else:
                print(f"{n.val} -> ", end = "")
            n = n.next
    
    def printLinkListBack(self):
        n = self.tail
        while n:
            if not n.prev:
                print(f"{n.val}")
            else:
                print(f"{n.val} <- ", end = "")
            n = n.prev

if __name__ == "__main__":
    nums = [i for i in range(10)]
    ll = DoublyLinkList()
    for i in nums[:5]:
        ll.addNodeLast(i)
    ll.printLinkList()
    for i in nums[5:]:
        ll.addNodeFirst(i)
    ll.printLinkList()
    print(ll.head.val)
    ll.printLinkListBack()
            
         