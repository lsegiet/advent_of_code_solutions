class Node:
    # Function to initialize the node object
    def __init__(self, v):
        self.val = v  # Assign value
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize next as null


# Doubly Linked List class
class DoublyLinkedList:
    # Function to initialize the Linked List
    def __init__(self, v):
        self.current = Node(v)
        self.current.next = self.current
        self.current.prev = self.current
        self.nodes = [self.current]

    def insert(self, v):
        temp = self.current.next
        self.current.next = Node(v)
        self.current.next.prev = self.current
        self.current.next.next = temp
        self.current.next.next.prev = self.current.next
        self.current = self.current.next

    def move_front(self, n=1):
        self.current = self.current.next
        if n > 1:
            self.move_front(self, n-1)

    def move_back(self, n=1):
        self.current = self.current.prev
        if n > 1:
            self.move_back(n-1)

    def delete(self):
        self.current.next.prev = self.current.prev
        self.current.prev.next = self.current.next
        v = self.current.val
        self.current = self.current.next
        return v


players = 452
marbles = 7125000
game = DoublyLinkedList(0)

scores = [0 for i in range(players)]
for i in range(1, marbles+1):
    if i % 23 == 0:
        scores[i % players] += i
        game.move_back(7)
        scores[i % players] += game.delete()
    else:
        game.move_front()
        game.insert(i)
print(max(scores))
