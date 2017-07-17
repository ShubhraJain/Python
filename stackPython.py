class stack():
    """
    Stack data structure implementation using python
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
            a = self.items[len(self.items) - 1]
            self.items.pop()
            return a

if __name__ == '__main__':
    st = stack()
    print(st.push(1))
    print(st.push('haha'))
    print(st.push(3))
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())