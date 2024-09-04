class Stack:
    def __init__(self):
        self.data = []

    def is_empty(self):
        # return len(self.data) == 0
        return not self.data  # more pythonic

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

    def size(self):
        return len(self.data)

    def __str__(self):
        """
        Returns str representation of the stack object
        """
        return (str(self.data))
