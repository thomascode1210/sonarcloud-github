import unittest
from src.main import greet_user, calculate_sum

class TestMain(unittest.TestCase):
    def test_greet_user(self):
        self.assertEqual(greet_user("Tuấn Anh"), "Xin chào, Tuấn Anh!")
        self.assertEqual(greet_user(""), "Xin chào, bạn!")

    def test_calculate_sum(self):
        self.assertEqual(calculate_sum(3, 4), 7)
        self.assertEqual(calculate_sum(-1, 1), 0)

if __name__ == "__main__":
    unittest.main()
