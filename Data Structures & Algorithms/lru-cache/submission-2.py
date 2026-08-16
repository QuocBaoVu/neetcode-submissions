class ListNode:
    def __init__(self, key=0, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev
class LRUCache:

    def __init__(self, capacity: int):
        # table to keep track of the key-node pair
        self.table = defaultdict(int)

        # Create a double linked-list
        self.tail = ListNode()
        self.head = ListNode(next=self.tail)
        self.tail.prev = self.head

        self.cap = capacity
    
    def add_to_last(self, new_node):
        # the last node (tail node is just dummu) 
        last_node = self.tail.prev 

        # new prev node of tail is new_node
        self.tail.prev = new_node

        # new node next is tail dummy
        new_node.next = self.tail

        # last node next is new_node
        last_node.next = new_node

        # new_node prev node is last_node
        new_node.prev = last_node


    def remove_node(self, node):
        # remove old node
        node.prev.next = node.next
        node.next.prev = node.prev


    def get(self, key: int) -> int:
        if key in self.table:
            # If there is key 
            # record the value
            node = self.table[key]
            self.remove_node(node)
            self.add_to_last(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        
        if key in self.table:
            node = self.table[key]
            node.val = value

            self.remove_node(node)
            self.add_to_last(node)
        else:
            if len(self.table) >= self.cap:

                first_node = self.head.next
                # delete that key-value pair from the table
                del self.table[first_node.key]
                self.remove_node(first_node)

            node = ListNode(key, value)
            self.table[key] = node
            self.add_to_last(node)


