"""
Data Structures & Algorithms - Stacks and Queues
Author: Juzer Tezabwala
Description: Robust OOP implementations of Linear Stack, Queue, and Circular Queue data structures.
"""

class Stack:
    """LIFO (Last-In-First-Out) Stack Implementation."""
    def __init__(self, max_size: int = 100):
        self._items = []
        self._max_size = max_size

    def push(self, item) -> bool:
        if self.is_full():
            print("⚠️ Stack Overflow: Cannot push onto full stack.")
            return False
        self._items.append(item)
        return True

    def pop(self):
        if self.is_empty():
            print("⚠️ Stack Underflow: Cannot pop from empty stack.")
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self._max_size

    def size(self) -> int:
        return len(self._items)

    def display(self):
        print("Stack (Top -> Bottom):", list(reversed(self._items)))


class Queue:
    """FIFO (First-In-First-Out) Queue Implementation."""
    def __init__(self, max_size: int = 100):
        self._items = []
        self._max_size = max_size

    def enqueue(self, item) -> bool:
        if self.is_full():
            print("⚠️ Queue Overflow: Cannot enqueue into full queue.")
            return False
        self._items.append(item)
        return True

    def dequeue(self):
        if self.is_empty():
            print("⚠️ Queue Underflow: Cannot dequeue from empty queue.")
            return None
        return self._items.pop(0)

    def peek(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def is_full(self) -> bool:
        return len(self._items) >= self._max_size

    def size(self) -> int:
        return len(self._items)

    def display(self):
        print("Queue (Front -> Rear):", self._items)


class CircularQueue:
    """Fixed-Size Circular Queue with Front and Rear Pointers."""
    def __init__(self, capacity: int = 5):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = -1
        self.rear = -1

    def is_full(self) -> bool:
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self) -> bool:
        return self.front == -1

    def enqueue(self, data) -> bool:
        if self.is_full():
            print("⚠️ Circular Queue is Full!")
            return False
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = data
        return True

    def dequeue(self):
        if self.is_empty():
            print("⚠️ Circular Queue is Empty!")
            return None
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        return data

    def display(self):
        if self.is_empty():
            print("Circular Queue is Empty.")
            return
        elements = []
        curr = self.front
        while True:
            elements.append(self.queue[curr])
            if curr == self.rear:
                break
            curr = (curr + 1) % self.capacity
        print("Circular Queue (Front -> Rear):", elements)


def run_demo():
    print("=== Stack Demonstration ===")
    s = Stack(max_size=3)
    s.push(10)
    s.push(20)
    s.push(30)
    s.display()
    print("Popped item:", s.pop())
    s.display()

    print("\n=== Queue Demonstration ===")
    q = Queue(max_size=3)
    q.enqueue("Task A")
    q.enqueue("Task B")
    q.enqueue("Task C")
    q.display()
    print("Dequeued:", q.dequeue())
    q.display()

    print("\n=== Circular Queue Demonstration ===")
    cq = CircularQueue(capacity=3)
    cq.enqueue(100)
    cq.enqueue(200)
    cq.enqueue(300)
    cq.display()
    print("Dequeued from CQ:", cq.dequeue())
    cq.enqueue(400)
    cq.display()

if __name__ == "__main__":
    run_demo()
