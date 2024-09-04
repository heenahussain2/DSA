"""
In this implementation of queue we will use deque (double ended queue)
"""
from collections import deque


class Queue:
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item) -> None:
        self.items.append(item)

    def dequeue(self) -> object:
        return self.items.popleft()

    def size(self) -> int:
        return len(self.items)

    def peek(self) -> object:
        return self.items[0]

    def __str__(self) -> str:
        return str(self.items)


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue(1)
    q.enqueue(2)
    print(q)
    print(q.dequeue())
    print(q)
