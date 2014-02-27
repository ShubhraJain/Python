import unittest
import string_match

class TestStringMatch(unittest.TestCase):
   def test_stringmatch(self):
       self.assertEqual(3, string_match.string_match('xxcaazz', 'xxbaaz'))
       self.assertEqual(2, string_match.string_match('abc', 'abc'))
       self.assertEqual(0, string_match.string_match('abc', 'axc'))
       self.assertEqual(0, string_match.string_match('', 'hello'))
       self.assertEqual(1, string_match.string_match('hello', 'he'))
       self.assertEqual(3, string_match.string_match('abababaaaabbb', 'ab'))
    
if __name__ == '__main__':
    unittest.main()
