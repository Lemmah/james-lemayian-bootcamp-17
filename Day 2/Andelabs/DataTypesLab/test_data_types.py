import unittest
from data_types import data_type

class DataTypeTestCase(unittest.TestCase):

  def test_none_type(self):
    self.assertEqual('no value', data_type(None))

  def test_array_type(self):
    self.assertEqual(3, data_type([1, 2, 3]))

  def test_small_array_type(self):
    self.assertEqual(None, data_type([1, 2]))

  def test_small_booleans_type(self):
    self.assertEqual(True, data_type(True))

  def test_small_integer_type(self):
    self.assertEqual('less than 100', data_type(3))

  def test_large_integer_type(self):
    self.assertEqual('more than 100', data_type(200))

  def test_str_type(self):
    self.assertEqual(6, data_type('andela'))

if __name__ == '__main__':
        unittest.main()
