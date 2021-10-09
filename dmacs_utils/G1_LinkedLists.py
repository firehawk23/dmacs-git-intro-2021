class LLNode:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        node = LLNode(data)
        if self.head is None:
            self.head = node
            return
        curr = self.head
        while curr.next is not None:
            curr = curr.next
        curr.next = node
        return
    
    def find(self, val):
        while self.next is not None:
            if self.data == val:
                return "Found!"
        return "Not Found!"
