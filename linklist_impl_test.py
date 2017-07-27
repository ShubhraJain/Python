import unittest
import linklist_impl

class TestLinkListImpl(unittest.TestCase):

    def test_find(self):
        
        llist = linklist_impl.LinkList()
        n = llist.append(1)
        llist.push(linklist_impl.Node(7))
        llist.append(2)
        llist.append(3)
        llist.insert(4, n)
        llist1 = linklist_impl.LinkList()
        llist1.push(linklist_impl.Node(6))
        
        self.assertIsNone(llist1.find(8))
        self.assertEqual(4, llist.find(4).value)
        self.assertIsNone(llist.find(6))


if __name__ == "__main__":
    unittest.main()


