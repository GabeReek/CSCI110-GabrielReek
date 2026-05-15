import os
import unittest

import final


class TestNumberQuest(unittest.TestCase):

    def test_get_hint(self):
        self.assertEqual(final.get_hint(10, 5), "Too low.")
        self.assertEqual(final.get_hint(10, 15), "Too high.")
        self.assertEqual(final.get_hint(10, 10), "Correct!")

    def test_calculate_score(self):
        self.assertEqual(final.calculate_score(1), 100)
        self.assertEqual(final.calculate_score(5), 60)
        self.assertEqual(final.calculate_score(20), 10)

    def test_is_valid_guess(self):
        self.assertTrue(final.is_valid_guess("7", 1, 20))
        self.assertFalse(final.is_valid_guess("hello", 1, 20))
        self.assertFalse(final.is_valid_guess("0", 1, 20))
        self.assertFalse(final.is_valid_guess("21", 1, 20))

    def test_save_and_read_high_score(self):
        test_file = "test_score.txt"

        final.save_high_score(test_file, 80)
        self.assertEqual(final.read_high_score(test_file), 80)

        os.remove(test_file)


if __name__ == "__main__":
    unittest.main()
