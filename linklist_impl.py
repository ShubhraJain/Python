class Node():

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
    
    def __str__(self):
        return "%d" % (self.value)


class LinkList():
    """
    Linklist data structure implementation
    """

    def __init__(self):
        self.head = None

    def push(self, nd):
        """
        This function takes a node as an argument and 
        makes it head of the linklist and points to the 
        existing head of the linklist
        """
        if not self.head:
            self.head = nd
        else:
            a = self.head
            self.head = nd
            self.head.next = a

    def append(self, value):
        """
        This function takes a value, converts it into a 
        node, appends it at the end of the linklist
        and returns the appended node
        """
        new_node = Node(value)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node
        return new_node

    def insert(self, value, prev_node):
        """
        This function creates a node from the given 
        value argument and inserts it next to the 
        given previous node
        """
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def find(self, value):
        """
        This function takes a value to be found in the 
        existing linklist and returns node if it's found 
        else returns None
        """
        if not self.head:
            return None
        else:
            cur = self.head
            while cur:
                if value == cur.value:
                    return Node(value)
                else:
                    cur = cur.next
            return None

    def tail(self):
        """
        Returns the node at the tail of the linklist
        """
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current

    def print(self):
        """
        prints the linklist
        """
        if not self.head:
            return "None"
        else:
            cur = self.head
            while cur:
                print(cur, " ", end = '')
                cur = cur.next
        print("")


llist = LinkList()
llist1 = LinkList()
llist1.push(Node(6))
# n = Node(5)
# llist.push(n)
n = llist.append(1)
llist.push(Node(7))
llist.append(2)
llist.append(3)
llist.insert(4, n)
print(llist.find(4))