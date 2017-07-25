class queue():
    """
    Queue data structure implementation using python
    """

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        return self.items

    def pop(self):
        if not self.items:
            return None
        else:
            a = self.items[0]
            del self.items[0]
            return a

if __name__ == '__main__':
    q = queue()
    print(q.push(1))
    print(q.push('haha'))
    print(q.push(3))
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.items)
