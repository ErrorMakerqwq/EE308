import unittest
import main


class TestcountingKwords(unittest.TestCase):

    def test_countingKwords(self):

        self.assertEqual(len(main.countingKwords(path="File.c")), 35)  # add assertion here


if __name__ == '__main__':
    unittest.main()

