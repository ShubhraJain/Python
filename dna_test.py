import unittest
import dna

class TestDna(unittest.TestCase):
   def get_length_test(self):
      self.assertEqual(6, get_length('ATCGAT'))
      self.assertEqual(0, get_length(''))

   def is_longer_test(self):
      self.assertTrue(is_longer('ATCG', 'AT'))

if __name__ == '__main__':
   unittest.main()
