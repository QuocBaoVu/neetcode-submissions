class ListNode():
    
    def __init__(self, key=None, value=None, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        # hashtable
        self.cap = capacity
        self.table = {}
        self.head = ListNode()
        self.tail = ListNode(prev=self.head)
        self.head.next = self.tail

    def delete(self, node):
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

    def add_to_tail(self, node):
        prev = self.tail.prev
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        prev.next = node

    
    def get(self, key: int) -> int:
        if key in self.table:
            node = self.table[key]
            self.delete(node)
            self.add_to_tail(node)
            return node.value            
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            node = self.table[key]
            node.value = value
            self.delete(node)
            self.add_to_tail(node)
        else:
            if len(self.table) == self.cap:
                head = self.head.next
                self.delete(head)
                del self.table[head.key]
            node = ListNode(key=key, value=value)
            self.add_to_tail(node)
            self.table[key] = node


        
