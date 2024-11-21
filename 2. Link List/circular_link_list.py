from typing import Optional

class Node:
    def __init__(self, val:any, next = None):
        self.val = val
        self.next:Optional[Node] = next
    
class circularSinglyLinkList:
    def __init__(self, head:Optional[Node] = None):
        self.head:Optional[Node] = head
        self.tail:Optional[Node] = head
        self.size:int = 0

    def isEmpty(self) -> bool:
        return self.head is None
    
    def addNodeLast(self, val:any) -> None:
        n = Node(val)
        if self.isEmpty():
            self.head = self.tail = n
            self.tail.next = self.head
        else:
            self.tail.next = n
            self.tail = self.tail.next
            self.tail.next = self.head
        self.size += 1

    def addNodeFirst(self, val:any)-> None:
        n = Node(val)
        if self.isEmpty():
            self.head = self.tail = n
        else:
            n.next = self.head
            self.head = n
            self.tail.next = self.head

        self.size += 1

    def __iter__(self):
        n = self.head
        while n:
            yield n.val
            n = n.next
            if n == self.head:
                break

    def __str__(self):
        return " -> ".join(map(str, self)) if not self.isEmpty() else "Empty List"

if __name__ == "__main__":
    nums = [i for i in range(10)]
    ll = circularSinglyLinkList()
    for i in nums[:5]:
        ll.addNodeLast(i)
    print(ll)
    for i in nums[5:]:
        ll.addNodeFirst(i)
    print(ll)
    print(ll.head.val)
            
         