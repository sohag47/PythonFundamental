import unittest
from average import average

class Test(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)

unittest.main()


print(dir(unittest))