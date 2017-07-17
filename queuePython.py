class queue():

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        return self.items

    def pop(self):
        if len(self.items) < 1:
            print("Queue is empty")
        else:
            del self.items[0]
            return self.items

if __name__ == '__main__':
    q = queue()
    print(q.push(1))
    print(q.push('haha'))
    print(q.push(3))
    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())