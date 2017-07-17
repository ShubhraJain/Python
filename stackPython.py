class stack():

    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)
        return self.items

    def pop(self):
        if len(self.items) < 1:
            print("Stack is empty")
        else:
            self.items.pop()
            return self.items

if __name__ == '__main__':
    st = stack()
    print(st.push(1))
    print(st.push('haha'))
    print(st.push(3))
    print(st.pop())
    print(st.pop())
    print(st.pop())
    print(st.pop())