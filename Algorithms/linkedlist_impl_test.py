import unittest
from linklist_impl import Node, LinkList

class TestLinkListImpl(unittest.TestCase):
    
    # def test_find(self):
        
        # self.assertIsNone(llist1.find(8)) 
        # self.assertEqual(4, llist.find(4).value) #Compares given value to found node's value
        # self.assertIsNone(llist.find(6)) #Element not present in the list
        # self.assertIsNone(llist2.find(1)) #finding in empty linkedlist

    def test_single_node_not_looped(self):
        l = LinkList()
        l.push(Node(1))
        self.assertFalse(l.is_looped())

    def test_single_node_looped(self):
        l = LinkList()
        n1 = Node(1)
        l.append(n1)
        n1.next = n1
        self.assertTrue(l.is_looped())

    def test_two_node_list_not_looped(self):
        l = LinkList()
        l.append(Node(1))
        l.append(Node(2))
        self.assertFalse(l.is_looped())

    def test_node_looped_on_itself(self):
        """
        Creates 3 node linkedlist where one of the nodes point to itself
        """
        l = LinkList()
        l.append(Node(1))
        l.append(Node(2))
        n1 = Node(3)
        l.append(n1)
        n1.next = n1
        self.assertTrue(l.is_looped())

    def test_multiple_node_not_looped(self):
        """
        Creates unlooped list of 6 nodes
        1--2--3--4--5--6 
        """
        l = LinkList()
        l.append(Node(1))
        l.append(Node(2))
        l.append(Node(3))
        n = Node(4)
        l.append(n)
        l.append(Node(5))
        n6 = Node(6)
        l.append(n6)
        self.assertFalse(l.is_looped())

    def test_long_looped_list(self):
        """
        Creates a looped list of 6 nodes
        1-2-3-4-5-6-4
        """
        l = LinkList()
        l.append(Node(1))
        l.append(Node(2))
        l.append(Node(3))
        n = Node(4)
        l.append(n)
        l.append(Node(5))
        n6 = Node(6)
        l.append(n6)
        n6.next = n
        self.assertTrue(l.is_looped())

    def test_looped_on_head(self):
        """
        Creates a list of 4 nodes where one of the nodes point to head
        """
        l = LinkList()
        head = Node(1)
        l.append(head)
        l.append(Node(2))
        l.append(Node(3))
        n1 = Node(4)
        l.append(n1)
        n1.next = head        
        self.assertTrue(l.is_looped())

if __name__ == "__main__":
    unittest.main()


