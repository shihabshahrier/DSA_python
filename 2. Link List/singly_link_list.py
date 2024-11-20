class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next
    
class SinglyLinkList:
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
            self.tail = self.tail.next
    def addNodeFirst(self, val):
        n = Node(val)
        if not self.head:
            self.head = n
            self.tail = n
        else:
            n.next = self.head
            self.head = n
    def printLinkList(self):
        n = self.head
        while n:
            if not n.next:
                print(f"{n.val}")
            else:
                print(f"{n.val} -> ", end = "")
            n = n.next

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
            
         