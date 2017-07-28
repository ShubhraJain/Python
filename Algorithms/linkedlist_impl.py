class Node():

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node
    
    def __str__(self):
        return "%d" % (self.value)


class LinkList():
    """
    Linkedlist data structure implementation
    """

    def __init__(self):
        self.head = None

    def push(self, nd):
        """
        This function takes a node as an argument and 
        makes it head of the linkedlist and points to the 
        existing head of the linkedlist
        """
        if not self.head:
            self.head = nd
        else:
            a = self.head
            self.head = nd
            self.head.next = a

    def append(self, nd):
        """
        This function takes a value, converts it into a 
        node, appends it at the end of the linkedlist
        and returns the appended node
        """
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = nd
        else:
            self.head = nd
        return nd

    def insert(self, value, prev_node):
        """
        This function creates a node from the given 
        value argument and inserts it next to the 
        given previous node in the linkedlist
        """
        new_node = Node(value)
        new_node.next = prev_node.next
        prev_node.next = new_node
        return new_node

    def find(self, value):
        """
        This function takes a value to be found in the 
        existing linkedlist and returns node if it's found 
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
        Returns the node at the tail of the linkedlist
        """
        if not self.head:
            return None
        current = self.head
        while current.next:
            current = current.next
        return current

    def print(self):
        """
        prints the linkedlist
        """
        if not self.head:
            return "None"
        else:
            cur = self.head
            while cur:
                print(cur, " ", end = '')
                cur = cur.next
        print("")

    def is_looped(self):
        """
        Returns true if linked list has a loop
        """
        next_pointer_list = []
        if not self.head:
           return None
        cur = self.head
        while cur:
           if cur.next not in next_pointer_list:
               next_pointer_list.append(cur.next)
               cur = cur.next
           else:
               return True
        return False

