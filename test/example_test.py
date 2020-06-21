import unittest

from src.example import give_me_a_true


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, give_me_a_true())


if __name__ == '__main__':
    unittest.main()
