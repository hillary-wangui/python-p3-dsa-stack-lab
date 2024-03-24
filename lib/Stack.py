class Stack:
    def __init__(self, limit=None):
        self.data = []
        self.limit = limit

    def push(self, value):
        if self.limit and len(self.data) >= self.limit:
            raise Exception("Stack is full")
        self.data.append(value)
        return self

    def pop(self):
        if not self.data:
            return None
        return self.data.pop()

    def peek(self):
        if not self.data:
            return None
        return self.data[-1]

    def size(self):
        return len(self.data)

    def empty(self):
        return len(self.data) == 0

    def full(self):
        if not self.limit:
            return False
        return len(self.data) >= self.limit

    def search(self, value):
        if not self.data:
            return -1
        for idx, item in enumerate(self.data[::-1]):
            if item == value:
                return idx
        return -1