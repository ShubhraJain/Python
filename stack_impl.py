class stack():
    """
    Stack data structure implementation using python
    """

    def __init__(self):
        self.items = []

    def stack_length(self):
        """
        Finds length of the given stack
        """
        l = len(self.items)
        if not self.items:
            return "Empty Stack"
            
        elif l == 1:
            return(self.items[0])
        else:
            pass

    def push(self, value):
        """
        Push value to the stack
        """
        self.items.append(value)
        return self.items

    def pop(self):
         """
        Pops element from the stack
        """
        if not self.items:
            return None
        else:
            a = self.items[-1]
            self.items.pop()
            return a

    def peek(self):
        if not self.items:
            return None
        else:
            return self.items[-1]

    def min_element(self, stack_values):
        """
        Returns the smallest element in the stack
        """
        self.items = stack_values
        if not self.items:
            print("Empty Stack")
        else:
            self.stack_length()
            min_val = self.items[0]
            for i in self.items:
                if i < min_val:
                    min_val = i
            return min_val

if __name__ == '__main__':
    st = stack()
    print(st.min_element([10, 7, 9, 4, 5, 8]))
    print(st.min_element([]))
    print(st.min_element([6]))
    print(st.min_element([7, 4, 1, 2, 6]))
    # print(st.push(1))
    # print(st.push('haha'))
    # print(st.push(3))
    # print(st.pop())
    # print(st.pop())
    # print(st.pop())
    # print(st.pop())