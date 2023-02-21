import unittest

from pairs import findPairs


# test for findPairs method
class TestFindPairs(unittest.TestCase):
  def test_1(self):
    numbers = [1, 9, 5, 0, 20, -4, 12, 16, 7]
    sum = 12
    expected = set(['0, 12', '-4, 16', '5, 7'])
    result = set(findPairs(numbers, sum))
    self.assertEqual(result, expected)

  def test_2(self):
    numbers = [1, 3, 2, -3, 5, 8, 0, 4]
    sum = 5
    expected = set(['-3, 8', '0, 5', '1, 4', '2, 3'])
    result = set(findPairs(numbers, sum))
    self.assertEqual(result, expected)


if __name__ == '__main__':
  unittest.main()