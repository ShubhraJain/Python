import unittest
import min_list

class TestMinList(unittest.TestCase):

	def test_two_min_values(self):
		self.assertEqual("1st min value is 2 and 2nd min value is 7", 
			min_list.two_min_values([33, 45, 9, 7, 2, 8, 19, 10, 60, 32]))
		self.assertEqual("List is too small", 
			min_list.two_min_values([4]))
		self.assertEqual("1st min value is 1 and 2nd min value is 3", 
			min_list.two_min_values([3,1]))
		self.assertEqual("1st min value is 5 and 2nd min value is 9", 
			min_list.two_min_values([33, 5, 9]))
		

if __name__ == '__main__':
    unittest.main()